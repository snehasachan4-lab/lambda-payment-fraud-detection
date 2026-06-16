import pandas as pd

df = pd.read_csv("data/transactions.csv")

customer_summary = (
    df.groupby("customer_id")
      .agg(
          total_transactions=("transaction_id", "count"),
          total_amount=("amount", "sum"),
          avg_transaction_amount=("amount", "mean")
      )
      .reset_index()
)

customer_summary.to_csv(
    "data/customer_metrics.csv",
    index=False
)

print(customer_summary.head())
print(f"Total Customers: {len(customer_summary)}")
