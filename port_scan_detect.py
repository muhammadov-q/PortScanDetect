import argparse
import pyshark

from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument('--full', default=False, action=argparse.BooleanOptionalAction)

args = parser.parse_args()

file = Path(args.path)

if not file.exists():
    print("The target file or directory doesn't exist")
    raise SystemExit(1)
if not str(file).endswith(".pcap"):
    print("File is not .pcap \nPlease show path for .pcap file")
    raise SystemExit(1)
print("*** Scanning started ***\n**\n*")

capture = pyshark.FileCapture(file)
full = args.full

null_scan = {}
xmas_scan = {}
fin_scan = {}
half_open_scan = {}
closed_ports = {}
udp_scan = dict()
icmp_requests = []


def check_tcp_scan(flags, src_ip, dst_port):
    global closed_ports
    if flags == 0:
        # Null Scan
        if src_ip not in null_scan:
            null_scan[src_ip] = set()
        null_scan[src_ip].add(dst_port)
    elif flags == 41:  # FIN, PSH, URG flags set
        # Xmas Scan
        if src_ip not in xmas_scan:
            xmas_scan[src_ip] = set()
        xmas_scan[src_ip].add(dst_port)
    elif flags == 2:  # SYN flag set
        # Half-Open Scan (SYN without ACK)
        if src_ip not in half_open_scan:
            half_open_scan[src_ip] = set()
        half_open_scan[src_ip].add(dst_port)
    elif flags == 18:  # SYN and ACK flags set
        # Closed Port Response
        if src_ip not in closed_ports:
            closed_ports[src_ip] = 0
        closed_ports[src_ip] += 1


def scan():
    for packet in capture:
        if 'TCP' in packet:
            flags = int(packet.tcp.flags, 16)
            src_ip = packet.ip.src
            dst_port = packet.tcp.dstport
            check_tcp_scan(flags, src_ip, dst_port)
        elif 'UDP' in packet:
            if 'ICMP' in packet:
                if packet.icmp.type == '3' and packet.icmp.code == '3':
                    # ICMP Port Unreachable - UDP Scan Detection
                    src_ip = packet.ip.src
                    dst_port = packet.icmp.udp_dstport
                    if src_ip not in udp_scan:
                        udp_scan[src_ip] = set()
                    udp_scan[src_ip].add(dst_port)
        elif 'ICMP' in packet:
            if packet.icmp.type == '8':  # Echo Request
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                icmp_requests.append(f"{src_ip} -> {dst_ip}")


scan()


def print_scan_results(scan_dict, scan_name):
    print(f"{scan_name} Scan:")
    if not scan_dict:
        print("\tNone")
    else:
        for src_ip, ports in scan_dict.items():
            print(f"\tIP source: {src_ip}")
            if full:
                print(f"\tDestination ports: {sorted(ports)}")
            else:
                print(f"\t\tFound {len(ports)} ports\t***Please add --full flag to see full list of Ports***")
        print()


def print_closed_ports():
    print("Closed Ports:")
    if not closed_ports:
        print("\tNone")
    else:
        for src_ip, count in closed_ports.items():
            print(f"\tIP source: {src_ip} - Closed Ports Count: {count}")
    print()


print_closed_ports()
print_scan_results(null_scan, "Null")
print_scan_results(xmas_scan, "Xmas")
print_scan_results(half_open_scan, "Half-Open")
print_scan_results(udp_scan, "UDP")

print('ICMP Echo Requests:')
if not icmp_requests:
    print('\tNone')
else:
    print("\tSource/Destination")
    for request in icmp_requests:
        print(f"\t{request}")
