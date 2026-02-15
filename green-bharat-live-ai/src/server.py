from flask import Flask, jsonify
from flask_cors import CORS
import os
import json
import time

app = Flask(__name__)
CORS(app)

DATA_FILE = "data/live_stats.jsonl"
ALERTS_FILE = "data/alerts.jsonl"

def get_latest_data(filepath):
    """Reads the last line of a JSONL file."""
    if not os.path.exists(filepath):
        return {}
    
    with open(filepath, "rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
            
        last_line = f.readline().decode()
        if last_line:
            return json.loads(last_line)
    return {}

@app.route('/latest')
def latest():
    data = get_latest_data(DATA_FILE)
    return jsonify(data)

@app.route('/alerts')
def alerts():
    # In a real app we'd return a list of recent alerts
    # For now, just the latest one
    data = get_latest_data(ALERTS_FILE)
    return jsonify(data)

if __name__ == '__main__':
    print("Starting Dashboard Server on port 5000...")
    app.run(host='0.0.0.0', port=5000)
