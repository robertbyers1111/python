#!/usr/bin/python3

import socket
import os

#pcap = []
#pcap =[i**2 for i in range(25)]
#for item in pcap:
#    print('pkt:',item)

# host to listen on
host = "10.0.0.5"

# create a raw socket and bind it to the public interface
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))

# we want the IP headers included in the capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# if we're using Windows, we need to send an IOCTL
# to set up promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

pkt0 = sniffer.recvfrom(65565)
print('type(pkt0):',type(pkt0))

pkt1 = sniffer.recvfrom(65565)
print('type(pkt1):',type(pkt1))

pkts = []
pkts = [pkt0, pkt1]

print('type(pkts):',type(pkts))

for pkt in pkts:
  print('pkt:',pkt)

# if we're using Windows, turn off promiscuous mode
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
