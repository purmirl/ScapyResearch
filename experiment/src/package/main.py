"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""
from scapy.arch import get_if_list, route_add_loopback, get_windows_if_list
from scapy.config import conf
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Loopback
from scapy.sendrecv import send, sendp, sr1

# TCP
from scapy.supersocket import L3RawSocket
from scapy.volatile import RandShort


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
