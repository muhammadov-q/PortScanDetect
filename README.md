# PCAP Analyzer Web Application

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)](https://flask.palletsprojects.com/)
[![PyShark](https://img.shields.io/badge/PyShark-0.4.2.9-yellow.svg)](https://kiminewt.github.io/pyshark/)

## Table of Contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The **PCAP Analyzer Web Application** is a powerful and user-friendly tool designed for network analysts, security professionals, and enthusiasts. It allows users to upload PCAP files for detailed analysis, providing insights through summaries and interactive data.

A video showing the demo of the application:

![Demo of the feature](tests/demo.gif)

## Usage Of port_scan_detect.py

Run the script with the path to a `.pcap` file:

```bash
python port_scan_detect.py path/to/your/pcap/file.pcap
```

Use the `--full` flag for a detailed report of the ports scanned:

```bash
python port_scan_detect.py path/to/your/pcap/file.pcap --full
```

## Output

The script will display the following information:

- **Closed Ports**: Displays the number of closed ports for each IP.
- **Scan Types**: Lists the IP addresses and ports involved in Null, Xmas, and Half-Open scans.
- **UDP Scan**: Lists UDP scan attempts detected via ICMP responses.
- **ICMP Echo Requests**: Displays the source and destination IPs for ICMP Echo Requests.

## Example Output

```
*** Scanning started ***
**
*
Closed Ports:
    IP source: 192.168.1.1 - Closed Ports Count: 6

Null Scan:
    None

Xmas Scan:
    None

Half-Open Scan:
    IP source: 192.168.1.100
            Found 1660 ports    ***Please add --full flag to see full list of Ports***

UDP Scan:
    None

ICMP Echo Requests:
    Source/Destination
    192.168.1.100 -> 192.168.1.103
```



## Installation

### Prerequisites

- **Python 3.6+**
- **pip** (Python package installer)
- **tshark** (Part of Wireshark)

### Install Python Packages

```bash
pip install -r requirements.txt
```

*Alternatively, manually install the packages:*

```bash
pip install flask pyshark werkzeug
```

### Install tshark

- **Windows**: Download and install [Wireshark](https://www.wireshark.org/download.html).
- **macOS**:

  ```bash
  brew install wireshark
  ```

- **Linux**:

  ```bash
  sudo apt-get install wireshark
  ```

**Note**: Ensure `tshark` is added to your system's PATH.

## Usage

### Running the Application

```bash
python app.py
```

**Note**: For production, use a WSGI server like Gunicorn or uWSGI.

### Accessing the Application

Open your web browser and navigate to:

```
http://localhost:5001
```

### Uploading and Analyzing a PCAP File

1. **Upload**: Click on "Select PCAP File" or drag and drop your file into the upload area.
2. **Analyze**: The application will process the file and redirect you to the results page.
3. **View Results**:
   - **Scan Summary**: Shows results of various scans and analysis types.
   - **Interactive Data**: Visualize protocol distribution and IP frequencies.
4. **Switch Theme**: Use the toggle switch to switch between light and dark modes.

## File Structure

```
pcap-analyzer-web/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── upload.html
│   └── results.html
├── static/
│   ├── css/
│   │   ├── styles.css
│   │   └── dark_mode.css
│   ├── js/
│   │   └── main.js
├── uploads/
│   └── (Uploaded files stored here)
└── README.md
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit your changes**:

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the branch**:

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request**.

## Advanced Features

### Drag-and-Drop File Upload

- **Implementation**: Users can drag files onto the designated area, which highlights upon file hover.
- **Fallback**: For browsers that don't support drag-and-drop, users can click to select files.

### Upload Progress Bar

- **Functionality**: Visual feedback during file upload, showing percentage completion.
- **Technical Details**: Utilizes the `XMLHttpRequest` API's `progress` event.

### Breadcrumb Navigation

- **Purpose**: Enhances navigation by showing the user's current position within the app.
- **Implementation**: Uses Bootstrap's breadcrumb component.

### Interactive Charts

- **Libraries Used**: [Chart.js](https://www.chartjs.org/) for rendering charts.
- **Charts Included**:
  - **Protocol Distribution**: Pie chart showing the percentage of each protocol.
  - **Source IP Frequencies**: Bar chart displaying the number of packets from each source IP.

### DataTables Integration

- **Functionality**: Enhances the packet details table with features like pagination, searching, and sorting.
- **Implementation**: Utilizes [DataTables](https://datatables.net/) jQuery plugin.


## Feedback and Support

If you encounter any issues or have suggestions for improvement, please open an issue on the GitHub repository or contact me directly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub**: [muhammadov-q](https://github.com/muhammadov-q)
- **Email**: [muhammadov_q@auac.kg](mailto:muhammadov_q@auca.kg)
- **Website**: [Kobiljon.Tech](https://www.kobiljon.tech)

---

*Developed with ❤️ by [Kobiljon Muhammadov](https://github.com/muhammadov-q)*