#!/bin/bash

echo "🌿 Starting Green Bharat Live AI Setup..."

# 1. Check Python
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python 3.9 or 3.10."
    exit
fi

# 2. Create Virtual Environment
if [ ! -d ".venv" ]; then
    echo "Creating Virtual Environment..."
    python3 -m venv .venv
fi

# 3. Install Dependencies
echo "Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt

# 4. Check for .env
if [ ! -f ".env" ]; then
    echo "Creating placeholder .env file..."
    echo "OPENAI_API_KEY=your_key_here" > .env
fi

echo -e "\n✅ Setup Complete!"
echo "To start the demo, run: ./run_demo.sh"
