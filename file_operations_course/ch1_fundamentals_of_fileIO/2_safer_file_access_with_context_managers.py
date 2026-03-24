from datetime import datetime

daily_metrics = {
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "region": "West Coast Hub",
    "shipments_processed": 150,
    "delivery_failures": 5,
    "average_delivery_time_minutes": 45
}

# define the log file path
log_file_path = "logs/daily_metrics_log.log"

import os

if not os.path.exists("logs"):
    os.makedirs("logs")

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