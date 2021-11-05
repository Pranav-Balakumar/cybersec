#/usr/local/bin/python3
from scapy.all import Ether, sr1, ICMP, IP
import sys

p=sr1(IP(dst=sys.argv[1])/ICMP())
if p:
    p.show()
