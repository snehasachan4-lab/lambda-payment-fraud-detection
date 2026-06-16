import pandas as pd
import json
from kafka import KafkaProducer

# Create Kafka Producer

producer = KafkaProducer(
bootstrap_servers='localhost:9092',
value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Read CSV file

df = pd.read_csv('data/transactions.csv')

# Send each transaction to Kafka

for _, row in df.iterrows():
    producer.send(
        'transactions',
        row.to_dict()
    )

# Ensure all messages are sent

producer.flush()

print(f"Sent {len(df)} transactions to Kafka")
