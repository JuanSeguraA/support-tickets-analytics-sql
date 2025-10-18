-- Check tickets without an agent or customer 
SELECT COUNT(*) 
FROM Tickets
WHERE agent_id IS NULL OR customer_id IS NULL;

-- Check customers that have the same first name and last name
SELECT first_name, last_name, COUNT(*) 
FROM Customers
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;


-- Check for duplicate customer_ids
SELECT customer_id, COUNT(*)
FROM Customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Check for duplicate ticket_ids
SELECT ticket_id, COUNT(*)
FROM Tickets
GROUP BY ticket_id
HAVING COUNT(*) > 1;

-- Check for duplicate escalation_id
SELECT escalation_id, COUNT(*)
FROM Escalations
GROUP BY escalation_id
HAVING COUNT(*) > 1;

-- No need to check for duplicate agent IDs since only has 20 records

-- Check for tickets that have been resolved before their creation
SELECT ticket_id
FROM tickets
WHERE resolved_at < created_at;