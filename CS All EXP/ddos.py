import socket
import struct
from datetime import datetime

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
ip_counter = {}
file_txt = open("attack_DDoS.txt", 'a')

No_of_IPs = 15  # Threshold for number of packets per IP

print("[*] Monitoring incoming packets...")

while True:
    pkt = s.recvfrom(2048)
   
    ip_header = pkt[0][14:34]
    ip_hdr = struct.unpack("!8sB3s4s4s", ip_header)
    src_ip = socket.inet_ntoa(ip_hdr[3])
   
    print("Source IP:", src_ip)
   
    if src_ip in ip_counter:
        ip_counter[src_ip] += 1
    else:
        ip_counter[src_ip] = 1

    if ip_counter[src_ip] > No_of_IPs:
        alert = f"DDoS attack is Detected from IP: {src_ip}"
        print("🚨", alert)
        file_txt.write(f"{datetime.now()} - {alert}\n")
        file_txt.flush()  # Save to file immediately

