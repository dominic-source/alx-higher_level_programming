-- find the average temperature
SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
ORDER BY value
