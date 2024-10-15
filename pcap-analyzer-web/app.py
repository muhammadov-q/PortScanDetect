from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
import pyshark
import os
import uuid
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure, random key in production

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 256 * 1024 * 1024  # 256MB max upload size
ALLOWED_EXTENSIONS = {'pcap', 'pcapng'}

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for file upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if file is in request
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Check if file is selected
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # Validate file and process
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_ext = os.path.splitext(filename)[1]
            unique_filename = str(uuid.uuid4()) + file_ext
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)
            try:
                scan_data = analyze_pcap(file_path)
            except Exception as e:
                logger.error(f"Error analyzing pcap: {e}")
                flash('Error analyzing the uploaded file. Please make sure it is a valid PCAP file.')
                return redirect(request.url)
            # Render the results template with scan data
            return render_template('results.html', data=scan_data)
        else:
            flash('Invalid file type. Please upload a .pcap or .pcapng file.')
            return redirect(request.url)
    else:
        return render_template('upload.html')

# Function to analyze PCAP file
def analyze_pcap(file_path):
    capture = pyshark.FileCapture(file_path, decryption_key=None, encryption_type='WPA-PWD')
    scan_results = []

    # Initialize counters and data structures
    total_packets = 0
    tcp_packets = 0
    udp_packets = 0
    icmp_packets = 0
    other_packets = 0

    protocols = {}
    src_ips = {}
    dst_ips = {}

    packet_list = []

    # Loop through packets
    for packet in capture:
        total_packets += 1

        # Record protocols
        protocol = packet.highest_layer
        protocols[protocol] = protocols.get(protocol, 0) + 1

        # Source and Destination IPs
        if 'IP' in packet:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            src_ips[src_ip] = src_ips.get(src_ip, 0) + 1
            dst_ips[dst_ip] = dst_ips.get(dst_ip, 0) + 1
        else:
            src_ip = 'N/A'
            dst_ip = 'N/A'

        # Packet type counters
        if 'TCP' in packet:
            tcp_packets += 1
        elif 'UDP' in packet:
            udp_packets += 1
        elif 'ICMP' in packet:
            icmp_packets += 1
        else:
            other_packets += 1

        # Add packet to list for table
        packet_info = {
            'no': total_packets,
            'time': packet.sniff_time.strftime('%H:%M:%S'),
            'source': src_ip,
            'destination': dst_ip,
            'protocol': protocol,
            'length': packet.length,
            'info': packet.info if hasattr(packet, 'info') else ''
        }
        packet_list.append(packet_info)

    # Prepare data for charts and tables
    scan_data = {
        'total_packets': total_packets,
        'tcp_packets': tcp_packets,
        'udp_packets': udp_packets,
        'icmp_packets': icmp_packets,
        'other_packets': other_packets,
        'protocols': protocols,
        'src_ips': src_ips,
        'dst_ips': dst_ips,
        'packet_list': packet_list
    }

    # Close the capture to free resources
    capture.close()

    return scan_data

if __name__ == '__main__':
    # In production, use a WSGI server like Gunicorn or uWSGI
    app.run(debug=False, host='0.0.0.0', port=5001)
