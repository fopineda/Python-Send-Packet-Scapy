from scapy.all import IP, ICMP, sr1, ls
# sending packets using scapy

# creates and ip object, only worrying about the src and dst. Everything else is defaulted
ipLayer = IP(src="192.168.0.40", dst="www.google.com")

# prints out packet fields and values
# print(IpLayer.show())

# defaulted ICMP object
icmpReq = ICMP()

packet = ipLayer / icmpReq

# sr1 stands for send-receive-layer 1; it sends the packet and stored what is received in the variable
receivedPacket  = sr1(packet)

if receivedPacket:
    print(receivedPacket.show())