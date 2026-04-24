from kafka import KafkaProducer
import requests, json

API_KEY = "YOUR_API_KEY"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={API_KEY}"
data = requests.get(url).json()

for article in data['articles']:
    producer.send("ai_news", article)

producer.flush()
