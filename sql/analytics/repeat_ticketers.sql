-- Customers who have opened multiple tickets
SELECT c.customer_id, c.account_type, COUNT(*) AS ticket_count
FROM Tickets t 
JOIN Customers c 
ON t.customer_id = c.customer_id
GROUP BY c.customer_id, c.account_type
HAVING COUNT(*) > 1
ORDER BY ticket_count DESC;
