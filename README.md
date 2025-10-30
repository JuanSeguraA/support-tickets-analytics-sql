# Customer Support & Ticketing Analytics

## Project Overview 
This project simulates a customer support ticketing system. It makes use of artificial customer, agent, and tickets data to create a ticketing relational database. This database helps to track KPIs such as:
- Average response and resolution times
- Escalation and SLA breach rates
- Ticket trends by month and category
- High-volume customers 

Furthermore, ODBC is utilized to connect Power BI to the SQLite database. This allows the analytics to be presented in an interactive Power BI dashboard with the use of DAX formulas. 

## Tech Stack
- **SQLite** : Design and create a relational database
- **Python** (pandas, numpy, faker) : Generate realistic artificial data for each relation
- **SQL** : Data quality tests and analytical queries for business KPIs
- **Power BI** : Dashboard visualization (DAX measures and relationships)

## Dashboard Preview
<p align="left">
  <img src="dashboard\dashboard_preview.png" width="750">
</p>

## How to Run
1. Clone the repo
2. Run `etl/load.py` to populate the SQLite database
3. Open the `.pbix` file in Power BI Desktop
4. Explore relationships, measures, and visualizations

## Example SQL Queries 
```
1) 
SELECT T.agent_id, A.first_name, ROUND(AVG((JULIANDAY(T.first_response_at) - JULIANDAY(T.created_at)) * 24 * 60), 2) AS avg_response_time
FROM Tickets T
JOIN Agents A ON T.agent_id = A.agent_id
WHERE T.first_response_at IS NOT NULL
GROUP BY T.agent_id, A.first_name
ORDER BY avg_response_time ASC;

2) 
SELECT category, ROUND(AVG(monthly_ticket_count)) AS avg_tickets_per_month
FROM (
    SELECT category, strftime('%Y-%m', created_at) AS month, COUNT(*) as monthly_ticket_count
    FROM Tickets
    GROUP BY category, month
    )
GROUP BY category
ORDER BY avg_tickets_per_month DESC;

3) 
SELECT category, ROUND(100.0 * SUM(escalated_flag) / COUNT(*), 2) AS escalation_rate_pct
FROM Tickets
GROUP BY category
ORDER BY escalation_rate_pct DESC;
