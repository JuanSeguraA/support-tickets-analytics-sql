-- Average response time by agent 
SELECT T.agent_id, A.first_name, ROUND(AVG((JULIANDAY(T.first_response_at) - JULIANDAY(T.created_at)) * 24 * 60), 2) AS avg_response_time
FROM Tickets T
JOIN Agents A ON T.agent_id = A.agent_id
WHERE T.first_response_at IS NOT NULL
GROUP BY T.agent_id, A.first_name
ORDER BY avg_response_time ASC;
