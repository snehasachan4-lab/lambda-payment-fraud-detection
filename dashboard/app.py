import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Lambda Fraud Dashboard",
    layout="wide"
)

st.title("💳 Lambda Architecture Fraud Detection Dashboard")

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/frauddb"
)

customer_df = pd.read_sql(
    "SELECT * FROM customer_metrics",
    engine
)

merchant_df = pd.read_sql(
    "SELECT * FROM merchant_metrics",
    engine
)

fraud_df = pd.read_sql(
    "SELECT * FROM fraud_alerts",
    engine
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Customers",
        len(customer_df)
    )

with col2:
    st.metric(
        "Total Merchants",
        len(merchant_df)
    )

with col3:
    st.metric(
        "Fraud Transactions",
        len(fraud_df)
    )

st.subheader("Top Customers")

st.dataframe(
    customer_df.sort_values(
        "total_amount",
        ascending=False
    ).head(10)
)

st.subheader("Top Merchants")

st.dataframe(
    merchant_df.sort_values(
        "total_amount",
        ascending=False
    ).head(10)
)

st.subheader("Fraud Alerts Sample")

st.dataframe(
    fraud_df.head(20)
)