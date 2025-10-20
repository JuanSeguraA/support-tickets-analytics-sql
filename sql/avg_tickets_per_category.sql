-- Average number of tickets per month per category 
SELECT category, ROUND(AVG(monthly_ticket_count)) AS avg_tickets_per_month
FROM (
    SELECT category, strftime('%Y-%m', created_at) AS month, COUNT(*) as monthly_ticket_count
    FROM Tickets
    GROUP BY category, month
    )
GROUP BY category
ORDER BY avg_tickets_per_month DESC;