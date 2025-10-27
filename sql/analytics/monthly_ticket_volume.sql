-- Number of tickets per month
SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) AS total_tickets
FROM Tickets
GROUP BY month
ORDER BY month;

