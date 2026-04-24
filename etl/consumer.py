from kafka import KafkaConsumer
import json, psycopg2

consumer = KafkaConsumer(
    'ai_news',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = psycopg2.connect("dbname=ai_news user=postgres password=password")
cur = conn.cursor()

for msg in consumer:
    a = msg.value

    cur.execute("""
    INSERT INTO raw_news (source, author, title, description, url, published_at)
    VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        a['source']['name'],
        a.get('author'),
        a.get('title'),
        a.get('description'),
        a.get('url'),
        a.get('publishedAt')
    ))

    conn.commit()
