from kafka import KafkaProducer
import requests
import json
from config.config import API_KEY, KAFKA_BROKER, TOPIC

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# News API URL
url = f"https://newsapi.org/v2/everything?q=artificial intelligence&language=en&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

# Send each article to Kafka
for article in data.get('articles', []):
    producer.send(TOPIC, article)

producer.flush()
print("✅ Data sent to Kafka topic")
