from scapy.all import sniff, IP, Raw

def get_protocol_name(proto_num):
    if proto_num == 1:
        return "ICMP"
    elif proto_num == 6:
        return "TCP"
    elif proto_num == 17:
        return "UDP"
    else:
        return "Other"

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print("\n📦 Packet Captured:")
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)
        print("Protocol:", get_protocol_name(ip_layer.proto))

        if packet.haslayer(Raw):
            print("Payload:", packet[Raw].load)

sniff(prn=process_packet, count=20)