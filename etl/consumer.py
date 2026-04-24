from kafka import KafkaConsumer
import json
import psycopg2
from config.config import DB_CONFIG, KAFKA_BROKER, TOPIC

# Kafka Consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

# PostgreSQL Connection
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

print("✅ Consumer started. Waiting for data...")

for message in consumer:
    article = message.value

    try:
        cursor.execute("""
            INSERT INTO raw_news (source, author, title, description, url, published_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            article.get('source', {}).get('name'),
            article.get('author'),
            article.get('title'),
            article.get('description'),
            article.get('url'),
            article.get('publishedAt')
        ))

        conn.commit()
        print("Inserted:", article.get('title'))

    except Exception as e:
        print("❌ Error:", e)
        conn.rollback()

cursor.close()
conn.close()
