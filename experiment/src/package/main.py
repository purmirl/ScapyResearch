"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""



# ARP
from scapy.layers.l2 import Ether, ARP

client_mac = ""
source_protocol_address = ""
destination_protocol_address = ""
arp_packet = Ether(dst = client_mac) / ARP(op = "who-has", psrc = source_protocol_address, pdst = destination_protocol_address)


"""
destination_port = 135
tcp_flags = "S" # U, A, P, R, S, F

tcp_packet = IP(dst = destination_ip) / TCP(sport = source_port, dport = destination_port, flags = tcp_flags)
tcp_packet.show()

send(tcp_packet)
"""
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