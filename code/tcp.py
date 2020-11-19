"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Copyrights 2020 PeTrA. All rights reserved

 TCP Example

 TCP : Transmission Control Protocol
"""
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from scapy.volatile import RandShort

destination_ip = "127.0.0.1"
source_port = RandShort()
destination_port = 135
tcp_flags = "S" # U, A, P, R, S, F

tcp_packet = IP(dst = destination_ip) / TCP(sport = source_port, dport = destination_port, flags = tcp_flags)
tcp_packet.show()

send(tcp_packet)