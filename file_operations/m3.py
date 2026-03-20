import os
from datetime import datetime

# Globomantics - Access Log Processor (Line-by-Line)
log_file_path = "logs/shipment_access.log"

# ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# create sample access log data
with open(log_file_path, "w") as file:
    for i in range(1,101): # makes 100 log entries
        status = "SUCCESS" if i % 10 != 0 else "FAILURE" # every 10th entry is a failure
        file.write(f"EventID={1000+i} | Status={status} | Hub=West | Timestamp={datetime.now()}\n")

print(f"Simulated access log written to {log_file_path}")

# read the log file line by line and print failed shipments
print("\n=== Failed Shipments Detected ===")
failed_count = 0

log_file = open(log_file_path, "r")

for line in log_file:
    if "FAILURE" in line:
        print(line.strip())
        failed_count += 1

log_file.close()

print(f"\nTotal failed shipments: {failed_count}")

print("\n=== First 5 log entries ===")
log_file = open(log_file_path, "r")

for _ in range(5):
    print(log_file.readline().strip())

log_file.close()

#counts all lines in file and prints out total
with open(log_file_path, "r") as file:
    all_lines = file.readlines()
    print(f"\nTotal lines (using readlines): {len(all_lines)}")