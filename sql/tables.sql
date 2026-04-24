CREATE TABLE raw_news (
 id SERIAL PRIMARY KEY,
 source TEXT,
 author TEXT,
 title TEXT,
 description TEXT,
 url TEXT,
 published_at TIMESTAMP
);

CREATE TABLE enriched_news (
 id INT,
 sentiment_score FLOAT,
 sentiment_label TEXT
);

CREATE TABLE entities (
 article_id INT,
 entity TEXT,
 entity_type TEXT
);
