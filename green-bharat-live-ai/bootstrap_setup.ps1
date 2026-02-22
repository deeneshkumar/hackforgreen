# Green Bharat Live AI - Automated Windows Setup

Write-Host "🌿 Starting Green Bharat Live AI Setup..." -ForegroundColor Green

# 1. Check Python
$pythonVersion = python --version 2>&1
if ($null -eq $pythonVersion) {
    Write-Error "Python not found! Please install Python 3.9 or 3.10."
    exit
}
Write-Host "Using $pythonVersion"

# 2. Create Virtual Environment
if (!(Test-Path ".venv")) {
    Write-Host "Creating Virtual Environment..."
    python -m venv .venv
}

# 3. Install Dependencies
Write-Host "Installing dependencies..."
.\.venv\Scripts\pip install -r requirements.txt

# 4. Check for .env
if (!(Test-Path ".env")) {
    Write-Host "Creating placeholder .env file..."
    "OPENAI_API_KEY=your_key_here" | Out-File -FilePath .env
}

Write-Host "`n✅ Setup Complete!" -ForegroundColor Green
Write-Host "To start the demo, run: ./run_demo.ps1"
