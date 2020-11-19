"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""

from scapy.layers.inet import IP, UDP
from scapy.packet import Raw

# TCP
from scapy.sendrecv import send
from scapy.volatile import RandShort


destination_ip = "192.168.35.102"
source_port = RandShort()
destination_port = 22

udp_packet = IP(dst = destination_ip) / UDP(dport = destination_port) / Raw(load = "abc")
send(udp_packet)
"""
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send
from scapy.volatile import RandShort

destination_ip = "192.168.35.102"
source_port = RandShort()
destination_port = 74
tcp_flags = "F" # U, A, P, R, S, F

tcp_packet = IP(dst = destination_ip) / TCP(sport = source_port, dport = destination_port, flags = tcp_flags)
tcp_packet.show()

send(tcp_packet)
"""