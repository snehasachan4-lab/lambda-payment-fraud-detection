import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/frauddb"
)

customer_df = pd.read_csv("data/customer_metrics.csv")
merchant_df = pd.read_csv("data/merchant_metrics.csv")
fraud_df = pd.read_csv("data/fraud_alerts.csv")

customer_df.to_sql(
    "customer_metrics",
    engine,
    if_exists="replace",
    index=False
)

merchant_df.to_sql(
    "merchant_metrics",
    engine,
    if_exists="replace",
    index=False
)

fraud_df.to_sql(
    "fraud_alerts",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")
