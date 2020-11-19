"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Copyrights 2020 PeTrA. All rights reserved

 UDP Example

 UDP : User Datagram Protocol
"""

# UDP
from scapy.sendrecv import send
from scapy.volatile import RandShort


destination_ip = "192.168.35.102"
source_port = RandShort()
destination_port = 22

udp_packet = IP(dst = destination_ip) / UDP(dport = destination_port) / Raw(load = "abc")
send(udp_packet)