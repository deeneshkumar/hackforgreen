FROM python:3.11-slim

# Install system dependencies
# Pathway requires some system libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose ports for web server (5000) and potentially Pathway (8080)
EXPOSE 5000
EXPOSE 8080

# Default command (overridden in docker-compose)
CMD ["python", "src/pipeline.py"]
