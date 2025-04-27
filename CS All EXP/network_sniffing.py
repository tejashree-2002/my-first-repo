from scapy.all import sniff, IP, TCP, UDP, ICMP

# Mapping protocol numbers to names
proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

def packet_analyzer(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto_num = ip_layer.proto
        proto_name = proto_map.get(proto_num, str(proto_num))  # Map number to name

        print(f"\n[+] IP Packet: {src_ip} --> {dst_ip} | Protocol: {proto_name}")

        # Analyze TCP, UDP, ICMP
        if proto_name == "TCP" and packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"    [TCP] Source Port: {tcp_layer.sport} --> Destination Port: {tcp_layer.dport}")
        elif proto_name == "UDP" and packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"    [UDP] Source Port: {udp_layer.sport} --> Destination Port: {udp_layer.dport}")
        elif proto_name == "ICMP" and packet.haslayer(ICMP):
            icmp_layer = packet.getlayer(ICMP)
            print(f"    [ICMP] Type: {icmp_layer.type} Code: {icmp_layer.code}")

def main():
    print("Starting advanced packet sniffer...")
    sniff(prn=packet_analyzer, store=0)

if __name__ == "__main__":
    main()
