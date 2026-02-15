Write-Host "Starting Green Bharat Live AI System..." -ForegroundColor Green

# 1. Start Ingestion (Generates Data)
Write-Host "Launching Data Ingestion..."
Start-Process python -ArgumentList "src/ingest.py"

# 2. Start Pipeline (Pathway Processing)
Write-Host "Launching Pathway Pipeline..."
Start-Process python -ArgumentList "src/pipeline.py"

# 3. Start Backend Server (Flask)
Write-Host "Launching Dashboard Server..."
Start-Process python -ArgumentList "src/server.py"

# Wait a moment for server to start
Start-Sleep -Seconds 3

# 4. Open Dashboard
Write-Host "Opening Dashboard..."
Start-Process "frontend\index.html"
