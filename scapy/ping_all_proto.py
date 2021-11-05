#!/usr/bin/env python2

from scapy.all import *

def icmp_ping(destination):
    # regular ICMP ping
    ans, unans = sr(IP(dst=destination)/ICMP())
    return ans

def tcp_ping(destination, dport):
    # TCP SYN Scan
    ans, unans = sr(IP(dst=destination)/TCP(dport=dport,flags="S"))
    return ans

def udp_ping(destination):
    # ICMP Port unreachable error from closed port
    ans, unans = sr(IP(dst=destination)/UDP(dport=0))
    return ans

def answer_summary(answer_list):
    # example of lambda with pretty print
    answer_list.summary(lambda s, r: r.sprintf("%IP.src% is alive"))

def main():
    destination = sys.argv[1]
    print("** ICMP Ping **")
    ans = icmp_ping(destination)
    answer_summary(ans)
    print("** TCP Ping **")
    ans = tcp_ping(destination, 22)
    answer_summary(ans)
    print("** UDP Ping **")
    ans = udp_ping(destination)
    answer_summary(ans)

if __name__ == "__main__":
    main()
