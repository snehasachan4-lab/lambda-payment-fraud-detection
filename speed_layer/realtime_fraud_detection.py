import pandas as pd

df = pd.read_csv("data/transactions.csv")

fraud_transactions = df[
df["amount"] > 50000
]

fraud_transactions.to_csv(
"data/fraud_alerts.csv",
index=False
)

print(
f"Fraud Transactions Found: {len(fraud_transactions)}"
)

