from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import os

fake = Faker()

transactions = []

countries = ["India", "USA", "UK", "Germany", "Singapore"]
payment_methods = ["UPI", "Credit Card", "Debit Card", "Net Banking"]

for i in range(100000):
    transaction = {
        "transaction_id": f"TXN{i+1}",
        "customer_id": f"CUST{random.randint(1, 5000)}",
        "merchant_id": f"MER{random.randint(1, 500)}",
        "amount": round(random.uniform(100, 100000), 2),
        "country": random.choice(countries),
        "payment_method": random.choice(payment_methods),
        "timestamp": fake.date_time_between(
            start_date="-30d",
            end_date="now"
        )
    }

    transactions.append(transaction)

df = pd.DataFrame(transactions)

os.makedirs("data", exist_ok=True)

df.to_csv("data/transactions.csv", index=False)

print(f"Generated {len(df)} transactions")
print("Saved to data/transactions.csv")