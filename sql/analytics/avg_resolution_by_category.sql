-- The average resolution time per category
SELECT category, ROUND(AVG(JULIANDAY(resolved_at) - JULIANDAY(created_at)) * 24 * 60) AS avg_resolution_category
FROM Tickets
WHERE resolved_at IS NOT NULL 
GROUP BY category
ORDER BY avg_resolution_category ASC;