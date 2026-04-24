CREATE VIEW company_trends AS
SELECT
 publish_date,
 COUNT(*) FILTER (WHERE title ILIKE '%openai%') * 0.6 +
 AVG(sentiment_score) * 0.4 AS openai_score
FROM clean_news c
JOIN enriched_news e ON c.id = e.id
GROUP BY publish_date;
