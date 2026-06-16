import pandas as pd

df = pd.read_csv("data/transactions.csv")

merchant_summary = (
    df.groupby("merchant_id")
      .agg(
          total_transactions=("transaction_id", "count"),
          total_amount=("amount", "sum")
      )
      .reset_index()
)

merchant_summary.to_csv(
    "data/merchant_metrics.csv",
    index=False
)

print(merchant_summary.head())
print(f"Total Merchants: {len(merchant_summary)}")
