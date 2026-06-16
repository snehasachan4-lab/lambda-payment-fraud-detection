# Lambda Architecture Fraud Detection System

## Overview

This project demonstrates a complete Lambda Architecture implementation for real-time payment fraud detection.

The system processes payment transactions, identifies potentially fraudulent transactions through a Speed Layer, generates historical analytics through a Batch Layer, stores processed results in PostgreSQL, and visualizes insights using a Streamlit dashboard.

---

## Architecture

```text
Transaction Generator
        │
        ▼
   Kafka Producer
        │
        ▼
    Kafka Topic
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Speed Layer   Batch Layer
(Fraud)       (Analytics)
 │             │
 ▼             ▼
Fraud       Customer Metrics
Alerts      Merchant Metrics
 │             │
 └──────┬──────┘
        │
        ▼
   PostgreSQL
        │
        ▼
 Streamlit Dashboard
```

---
## Business Problem

Financial institutions process millions of transactions daily.

The objective is to detect suspicious transactions in near real-time while also generating historical analytics for customers and merchants.

Lambda Architecture is used to combine real-time processing with batch analytics.

## Tech Stack

- Python
- Apache Kafka
- PostgreSQL
- Docker
- Pandas
- SQLAlchemy
- Streamlit

---

## Project Structure

```text
lambda-payment-fraud-detection/
│
├── batch_layer/
│   ├── customer_analytics.py
│   └── merchant_analytics.py
│
├── dashboard/
│   └── app.py
│
├── producer/
│   ├── transaction_generator.py
│   └── kafka_producer.py
│
├── serving_layer/
│   └── load_to_postgres.py
│
├── speed_layer/
│   └── realtime_fraud_detection.py
│
├── data/
│   ├── transactions.csv
│   ├── fraud_alerts.csv
│   ├── customer_metrics.csv
│   └── merchant_metrics.csv
│
├── docker-compose.yml
└── consumer_test.py
```

---

## Dataset

Sample generated transaction dataset included.

### Statistics

| Metric | Value |
|----------|----------|
| Transactions | 100,000 |
| Customers | 5,000 |
| Merchants | 500 |
| Fraud Alerts | 49,964 |

### Files

- transactions.csv → Raw payment transactions
- fraud_alerts.csv → Fraudulent transactions detected by Speed Layer
- customer_metrics.csv → Customer level aggregations
- merchant_metrics.csv → Merchant level aggregations

---

## Components

### Producer Layer

Generates payment transactions and publishes them to Kafka.

Files:
- transaction_generator.py
- kafka_producer.py

---

### Speed Layer

Processes incoming transactions and identifies suspicious activities using fraud detection rules.

Output:
- fraud_alerts.csv

---

### Batch Layer

Performs historical aggregation and analytics.

Outputs:
- customer_metrics.csv
- merchant_metrics.csv

---

### Serving Layer

Loads processed datasets into PostgreSQL tables.

Tables:
- customer_metrics
- merchant_metrics
- fraud_alerts

---

### Dashboard

Built using Streamlit.

Dashboard Features:

- Total Customers
- Total Merchants
- Fraud Transactions
- Top Customers
- Top Merchants
- Fraud Alert Samples

---

## Running the Project

### Start Infrastructure

```bash
docker compose up -d
```

### Generate Transactions

```bash
python producer/transaction_generator.py
```

### Push Data to Kafka

```bash
python producer/kafka_producer.py
```

### Run Fraud Detection

```bash
python speed_layer/realtime_fraud_detection.py
```

### Generate Batch Analytics

```bash
python batch_layer/customer_analytics.py

python batch_layer/merchant_analytics.py
```

### Load Data to PostgreSQL

```bash
python serving_layer/load_to_postgres.py
```

### Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Results

Successfully implemented:

- Real-time Fraud Detection
- Lambda Architecture
- Kafka Data Ingestion
- Batch Analytics
- PostgreSQL Serving Layer
- Streamlit Dashboard

---

## Key Achievements

- Processed 100,000+ transactions
- Generated 49,964 fraud alerts
- Built Kafka-based ingestion pipeline
- Implemented Batch and Speed Layers
- Loaded analytics into PostgreSQL
- Created Streamlit monitoring dashboard

---

## Future Enhancements

- Spark Structured Streaming
- Machine Learning based Fraud Detection
- Airflow Orchestration
- S3 Data Lake Storage
- Grafana Monitoring

---
