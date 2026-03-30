from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent # Get the directory of the current file
log_file_path = BASE_DIR / "logs" / "daily_metrics_log.log" # Define the path to the metrics log file

daily_metrics = {
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "region": "West Coast Hub",
    "shipments_processed": 150,
    "delivery_failures": 5,
    "average_delivery_time_minutes": 45
}

# always makes sure directory exists
log_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Create a log entry string with the daily metrics
log_entry = (
    f"{daily_metrics['date']} "
    f"Regions: {daily_metrics['region']} | "
    f"Shipments: {daily_metrics['shipments_processed']} | "
    f"Failures: {daily_metrics['delivery_failures']} | "
    f"Average Delivery Time (minutes): {daily_metrics['average_delivery_time_minutes']} hrs\n"
)

# with lets us not have to close the file after writing to it, a for append mode
with open(log_file_path, "a") as log_file:
    log_file.write(log_entry)

print("Daily metrics logged successfully.")