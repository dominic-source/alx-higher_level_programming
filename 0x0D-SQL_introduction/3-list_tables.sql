-- list all the tables in a database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE()
