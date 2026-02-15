#!/bin/bash

echo "Starting Green Bharat Live AI System..."

# 1. Start Ingestion
echo "Launching Data Ingestion..."
python src/ingest.py &

# 2. Start Pipeline
echo "Launching Pathway Pipeline..."
python src/pipeline.py &

# 3. Start Backend Server
echo "Launching Dashboard Server..."
python src/server.py &

# Wait a moment
sleep 3

# 4. Open Dashboard
echo "Opening Dashboard..."
if which xdg-open > /dev/null; then
  xdg-open frontend/index.html
elif which open > /dev/null; then
  open frontend/index.html
fi
