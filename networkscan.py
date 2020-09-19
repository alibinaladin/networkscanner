import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("p.q.r.s/x")