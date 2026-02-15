import pathway as pw
import os
import datetime
# import alerts
# import rag

# Define data schema
class SensorData(pw.Schema):
    timestamp: str
    location: str
    pm25: float
    pm10: float
    co2: float
    temperature: float

# Constants
DATA_DIR = "data"
STREAM_FILE = os.path.join(DATA_DIR, "stream.csv")

def check_air_quality(pm25):
    if pm25 > 250:
        return "CRITICAL"
    elif pm25 > 120:
        return "HIGH" 
    elif pm25 > 90:
        return "MEDIUM"
    return "NORMAL"

def run_pipeline():
    # 1. Ingest Data (Streaming)
    # We use csv.read with mode="streaming" to tail the file
    data = pw.io.csv.read(
        DATA_DIR,
        schema=SensorData,
        mode="streaming",
        autocommit_duration_ms=1000
    )

    # 2. Process Data (Windowing)
    # Let's calculate a sliding average over the last 10 seconds to smooth out noise
    # We first parse the timestamp
    # Note: timestamps in CSV are strings, ensuring we parse them if needed or use processing time
    # For simplicity in this MVP, we might rely on processing time or just raw stream 
    
    # Simple alert logic on raw stream for instant reaction
    # Filter for alerts first (Robust)
    alert_data = data.filter(data.pm25 > 90)

    # Then format the output
    active_alerts = alert_data.select(
        timestamp=alert_data.timestamp,
        location=alert_data.location,
        pm25=alert_data.pm25,
        status=pw.apply(lambda x: "CRITICAL" if x > 250 else ("HIGH" if x > 120 else "MEDIUM"), alert_data.pm25),
        message=pw.apply(lambda x: f"High PM2.5 detected: {x}", alert_data.pm25)
    )

    # 3. Output to JSON for Frontend
    # The frontend will poll this or use Server-Sent Events if we set up a server
    # For simplicity, we write to a JSON lines file that the frontend can tail/poll
    # OR we use Pathway's HTTP server connector if available for easy verified output
    
    # Let's write to a file first, it's safer for a simple demo structure without complex networking
    pw.io.jsonlines.write(active_alerts, os.path.join(DATA_DIR, "alerts.jsonl"))
    pw.io.jsonlines.write(data, os.path.join(DATA_DIR, "live_stats.jsonl"))

    # 4. RAG / Indexing (Optional / Advanced)
    # This would go here.
    
    pw.run()

if __name__ == "__main__":
    run_pipeline()
