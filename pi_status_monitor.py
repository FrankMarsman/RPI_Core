import os
import time
from datetime import datetime

def ensure_log_directory():
    """Ensure the log directory exists."""
    log_dir = "/home/pi/C/logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

def write_online_status():
    """Write PI ONLINE status to log file every minute."""
    log_file = "/home/pi/C/logs/main_log.txt"
    
    # Ensure directory exists
    ensure_log_directory()
    
    # Main loop
    while True:
        try:
            # Get current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Write to log file
            with open(log_file, "a") as f:
                f.write(f"[{timestamp}] PI ONLINE\n")
            
            # Wait 60 seconds before next write
            time.sleep(60)
        
        except Exception as e:
            print(f"Error writing to log file: {e}")
            time.sleep(60)  # Wait before retrying

if __name__ == "__main__":
    write_online_status()