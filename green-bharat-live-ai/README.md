# Green Bharat Live AI: Real-Time Sustainability Monitoring & Alert System

**Powered by Pathway**

A real-time AI system that continuously ingests sustainability data (Pollution, CO2, Temperature), detects anomalies instantly, and provides explainable AI alerts using live RAG.

## 🚀 Features
- **Live Data Ingestion**: Simulates real-time sensor data (PM2.5, PM10, CO2).
- **Streaming Processing**: Uses Pathway for windowing, aggregation, and anomaly detection.
- **Instant Alerts**: Triggers alerts automatically when thresholds are breached.
- **Live RAG Explanation**: Explains alerts using a live document store (government guidelines, health impacts).
- **Real-Time Dashboard**: Updates instantly without page refreshes.

## 📂 Structure
- `src/`: Source code for ingestion, pipeline, and RAG.
- `docs/`: Knowledge base for the AI (PDFs, MDs).
- `frontend/`: Real-time dashboard.
- `data/`: Data streams.

## 🛠️ Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables (create `.env`):
   ```
   OPENAI_API_KEY=your_key_here
   ```
3. Run the data stream:
   ```bash
   python src/ingest.py
   ```
4. Run the Pathway pipeline:
   ```bash
   python src/pipeline.py
   ```

## 🐳 Docker Setup (Recommended for Windows)
Since Pathway runs best on Linux, Windows users should use Docker.

1. Ensure Docker Desktop is running.
2. Build and run:
   ```bash
   docker-compose up --build
   ```
3. Open Dashboard: http://localhost:8000

## 📜 License
MIT
