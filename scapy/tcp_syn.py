#!/usr/bin/env python3

from scapy.all import *
import sys
# def tcp_scan(destination, dport):
#     ans, unans = sr(IP(dst=destination)/TCP(sport=666,dport=dport,flags="S"))
#     for sending, returned in ans:
#         if 'SA' in str(returned[TCP].flags):
#             return destination + " port " + str(sending[TCP].dport) + " is open"
#         else:
#             return destination + " port " + str(sending[TCP].dport) + " is not open"

# argument 1: ip address of destinatin
# argument 2: port number (unused?)

def main():
    destination = sys.argv[1]
    port = int(sys.argv[2])
    ip = IP(dst=destination)
    syn_packet = ip/TCP(sport=1500, dport=port, flags="S", seq=100)
    print("Sending packet:")
    syn_packet.show()
    
    synack_pkt = sr1(syn_packet)
    print("received packet:")
    synack_pkt.show()

    my_ack = synack_pkt.seq+1
    ack_packet = ip/TCP(sport=1500, dport=port, flags="A", seq=101, ack=my_ack)
    print("sending packet:")
    ack_packet.show()
    send(ack_packet)

if __name__ == "__main__":
    main()


