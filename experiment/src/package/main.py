"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import send

# ICMP
destination_ip = "8.8.8.8"
data = "hello world"
icmp_packet = IP(dst = destination_ip) / ICMP() / data
icmp_packet.show()

send(icmp_packet)