from collections import defaultdict  # a dictionary, but it automatically creates an empty list if a new key is accessed.
from datetime import datetime     # For converting string timestamps to real date/time objects.

# Configuration
log_file = "network.log"
request_threshold = 5  # Requests per IP within the window to trigger alert
time_window = 5  # Time window in seconds

# Helper function to parse log line
def parse_log_line(line):
    try:
        time_str = line.split("]")[0].strip("[")
        ip = line.split("IP:")[1].split()[0]
        timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        return ip, timestamp
    except:
        return None, None

# Store IP request timestamps
ip_requests = defaultdict(list)

# Read log file and process requests
with open(log_file, "r") as file:
    for line in file:
        ip, timestamp = parse_log_line(line)
        if ip and timestamp:
            ip_requests[ip].append(timestamp)

# Analyze for DDoS behavior
print("\n=== DDoS Detection Report ===")
for ip, timestamps in ip_requests.items():
    timestamps.sort()
    for i in range(len(timestamps)):
        window_start = timestamps[i]
        count = 1
        for j in range(i+1, len(timestamps)):
            if (timestamps[j] - window_start).seconds <= time_window:
                count += 1
            else:
                break
        if count >= request_threshold:
            print(f"Potential DDoS detected from IP: {ip} — {count} requests in {time_window} seconds")
            break
print("=== End of Report ===")
