AI News Streaming Analytics Platform

 Overview
This project is an end-to-end **near real-time data engineering pipeline** that ingests AI-related news articles, processes them using streaming architecture, enriches them with NLP techniques, and delivers actionable insights through BI dashboards.

It simulates a **production-grade system** using Kafka, SQL-based transformations, and AI-driven analytics.

---

 Key Features

- Real-time ingestion** using Kafka (Producer & Consumer)
- PostgreSQL Data Warehouse** (Bronze → Silver → Gold layers)
- Sentiment Analysis** using VADER
- Entity Extraction** using spaCy (companies, people, tech)
- Trend Scoring Engine** (custom business logic)
- Data Quality Checks**
- AI Summarization Agent** (LLM-based insights)
- Tableau Dashboard for Visualization**

---

 Architecture
 
News API → Kafka Producer → Kafka Topic → Kafka Consumer → PostgreSQL

PostgreSQL Layers: Bronze (raw_news) ↓ Silver (clean_news) ↓ Feature Layer (sentiment + entities) ↓ Gold (trend analytics)

→ Tableau Dashboard → AI Summary Agent

---

Tech Stack

| Layer            | Technology |
|-----------------|-----------|
| Ingestion        | Python, Kafka |
| Storage          | PostgreSQL |
| Processing       | SQL |
| NLP              | VADER, spaCy |
| Streaming        | Kafka |
| Visualization    | Tableau |
| AI Agent         | OpenAI API |

---

Project Structure
ai-news-kafka-analytics/ │ ├── etl/ │   ├── producer.py │   ├── consumer.py │   ├── sentiment.py │   ├── entities.py │   └── summarizer.py │ ├── sql/ │   ├── 01_tables.sql │   ├── 02_clean.sql │   ├── 03_features.sql │   ├── 04_trends.sql │ ├── config/ │   └── config.py │ ├── dashboard/ │   └── tableau_guide.md │ ├── requirements.txt └── README.md
