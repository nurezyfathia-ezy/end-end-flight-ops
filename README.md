# Real-World End-to-End Flight Data Engineering Pipeline

A production-grade, near-real-time data engineering project that orchestrates live aviation data ingestion, processes it using a multi-layered Medallion Architecture, and delivers analytics-ready datasets for BI dashboards.

This project moves beyond basic DAG syntax to demonstrate how **Apache Airflow** is utilized in production—focusing on orchestration, robust scheduling, retries, idempotent pipelines, and dimensional data modeling.

---

##  Architecture & Data Flow

```text
[Live Flight API] 
       │
       ▼ (Airflow HTTP Operator / Python Execution)
┌────────────────────────────────────────────────────────┐
│                      BRONZE LAYER                      │
│            • Raw API JSON Response Ingestion           │
│            • Persistent raw storage landing            │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Transformation & Schema Enforcement)
┌────────────────────────────────────────────────────────┐
│                      SILVER LAYER                      │
│            • Data Cleaning & Normalization             │
│            • De-duplication & Type Casting             │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Aggregation & Metric Calculation)
┌────────────────────────────────────────────────────────┐
│                       GOLD LAYER                       │
│            • Pattern-level Aggregations                │
│            • Operational KPIs (Air traffic volume)     │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Idempotent UPSERT Logic)
               [PostgreSQL Analytics DB] 
                           │
                           ▼
              [BI Dashboards (Power BI)]
