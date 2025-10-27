-- Measures how often tickets exceed their SLA target resolution times, grouped by priority (e.g., Low, Medium, High, Urgent
SELECT priority, ROUND(
                        AVG(CASE 
                                WHEN ((JULIANDAY(resolved_at) - JULIANDAY(created_at)) * 24) > 
                                    CASE priority
                                        WHEN 'Low' THEN 72 
                                        WHEN 'Medium' THEN 48
                                        WHEN 'High' THEN 24
                                        ELSE 8
                                    END
                                THEN 1 ELSE 0
                            END
                        ), 2
                    ) AS breach_rate_per_cat
FROM Tickets
WHERE resolved_at is NOT NULL
GROUP BY priority
ORDER BY breach_rate_per_cat DESC;

                    

                    
                            