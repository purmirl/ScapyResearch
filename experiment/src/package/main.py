"""
 PeTrA's Scapy Research Laboratory 2020 ~
 Experiment

 Note

  01. (pip install scapy) or (pip install --pre scapy) in windows powershell or linux terminal
"""

from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

# icmp
r = sr1(IP(dst="8.8.8.8")/ICMP()/"HelloWorld")
r.show()
