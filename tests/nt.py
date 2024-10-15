import argparse
import pyshark

from pathlib import Path

parser = argparse.ArgumentParser()
# show_all = False
parser.add_argument("path")
parser.add_argument('--full', default=False,
                    action=argparse.BooleanOptionalAction)

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
full = parser.parse_args().full
null_scan = 0
xmas_scan = 0
fin_scan = 0
half_open = 0
closed_ports = 0
flags_arr = []
udp_scan = dict()
icmp = []


def check_tcp_scan():
    global null_scan
    global xmas_scan
    global half_open
    global fin_scan
    global closed_ports

    if '0' in flags_arr and '14' in flags_arr:
        null_scan += 1
        flags_arr.clear()
    if ('0' in flags_arr and '29' in flags_arr) or ('14' in flags_arr and '29' in flags_arr):
        xmas_scan += 1
        flags_arr.clear()
    if ('2' in flags_arr and '14' in flags_arr and '4' in flags_arr):
        half_open += 1
        flags_arr.clear()
    if ('2' in flags_arr and '14' in flags_arr):
        closed_ports += 1
        flags_arr.clear()
    if (('1' in flags_arr and '4' in flags_arr) or ('1' in flags_arr)):
        fin_scan += 1
        flags_arr.clear()


def scan():
    for f in capture:
        if 'tcp' in f:
            flags_arr.append(str(f.tcp.flags.raw_value))
            check_tcp_scan()
        # if 'udp' in f:
        #     if 'icmp' in f:
        #         print(str(f.icmp.type) == '3', str(f.icmp.code) == '3')
            # print(dir(f))
            # print(f.udp)
            # if ('icmp' in f):
            # print(f.pretty_print())
            # break
            # if f.udp.dstport:
            #     if str(f.ip.src_host) not in udp:
            #         udp[str(f.ip.src_host)] = set()

            #     udp[str(f.ip.src_host)].add(str(f.udp.dstport))
            # print("IP source: ", f.ip.src_host,
            #       " Host port: ", f.udp.port,
            #       " Destination port: ", f.udp.dstport)
            # print(dir(f.udp))
            # break
        if 'icmp' in f:

            if str(f.icmp.type) == '8':
                #   print("IP source: ", f.ip.src_host,
                #   " Destination port: ", f.udp.dstport)
                # print(dir(f.ip))
                icmp.append(str(f.ip.src) + " -> " + str(f.ip.dst))
            if str(f.icmp.type) == '3' and str(f.icmp.code) == '3':
                # print(f.icmp.udp_dstport)
                if str(f.ip.src_host) not in udp_scan:
                    udp_scan[str(f.ip.src_host)] = set()

                udp_scan[str(f.ip.src_host)].add(str(f.icmp.udp_dstport))


scan()


def print_icmp():
    print('ICMP Echo request: ',)
    if not icmp:
        print('\tNone')
    else:
        print("\tsource/destination")
        for k in icmp:
            print("\t", k)


def print_udp(full):
    print("UDP scan:", )
    if len(udp_scan.items()) == 0:
        print("\tNone")
    else:
        for k, v in udp_scan.items():
            print("\tIP source: ", k)
            print("\n\tDestination port:")
            if full:
                print(list(v))
            else:
                print("\t\tFound ", len(
                    list(v)), " ports\t***Please add --full flag to see full list of Ports***")
        print()


# if closed_ports > 0:
print("Closed Ports: %d" % closed_ports)
# if null_scan > 0:
print("Found Null Scan: %d" % null_scan)
# if xmas_scan > 0:
print("Found Xmas Scan: %d" % xmas_scan)
# if half_open > 0:
print("Found Half Open Scan: %d" % half_open)

# if udp_scan:
print_udp(full)

# if icmp:
print_icmp()
print("Found Fin Scan: %d" % fin_scan)