CREATE TABLE clean_news AS
SELECT *, DATE(published_at) AS publish_date
FROM raw_news
WHERE title IS NOT NULL;
