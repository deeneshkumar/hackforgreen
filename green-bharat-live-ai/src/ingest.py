import csv
import time
import random
import datetime
import os

# Configuration
DATA_DIR = "data"
STREAM_FILE = os.path.join(DATA_DIR, "stream.csv")
LOCATIONS = ["Chennai-Adyar", "Chennai-AnnaNagar", "Chennai-TNagar", "Chennai-Velachery"]

def generate_data():
    """Generates a single data point simulating a sensor reading."""
    location = random.choice(LOCATIONS)
    # Simulate normal ranges with occasional spikes
    pm25 = random.uniform(10, 60)
    pm10 = random.uniform(20, 100)
    co2 = random.uniform(300, 450)
    temp = random.uniform(25, 35)

    # Introduce anomalies randomly (10% chance)
    if random.random() < 0.1:
        pm25 += random.uniform(50, 150) # Spike
        pm10 += random.uniform(50, 150)
    
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "location": location,
        "pm25": round(pm25, 2),
        "pm10": round(pm10, 2),
        "co2": round(co2, 2),
        "temperature": round(temp, 2)
    }

def main():
    print(f"Starting data stream to {STREAM_FILE}...")
    
    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)
    
    # Initialize file with headers if it doesn't exist
    if not os.path.exists(STREAM_FILE):
        with open(STREAM_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "location", "pm25", "pm10", "co2", "temperature"])
            writer.writeheader()

    while True:
        data = generate_data()
        with open(STREAM_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "location", "pm25", "pm10", "co2", "temperature"])
            writer.writerow(data)
        
        print(f"Generated: {data}")
        time.sleep(1) # 1 data point per second

if __name__ == "__main__":
    main()
