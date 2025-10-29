-- The escalation rate per ticket category 
SELECT category, ROUND(100.0 * SUM(escalated_flag) / COUNT(*), 2) AS escalation_rate_pct
FROM Tickets
GROUP BY category
ORDER BY escalation_rate_pct DESC;