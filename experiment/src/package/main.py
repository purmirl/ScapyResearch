"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

# TCP
destination_ip = ""
destination_port = ""
tcp_flags = "" # U, A, P, R, S, F
tcp_packet = IP(dst = destination_ip) / TCP(dport = destination_port, flags = tcp_flags)

send(tcp_packet)