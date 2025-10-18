import sqlite3
import pandas as pd
import os

DB_PATH = r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\support_tickets.db"
SCHEMA_PATH = r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\schema\create_tables.sql"
DATA_PATH = r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

with open(SCHEMA_PATH, "r") as f:
    schema_sql = f.read()
cur.executescript(schema_sql)
print("Database schema created")

with open(SCHEMA_PATH, "r") as f:
    schema_sql = f.read()
print("Schema content preview:\n", schema_sql[:500])  
cur.executescript(schema_sql)

customers_df = pd.read_csv(os.path.join(DATA_PATH, "customers_raw.csv"))
agents_df = pd.read_csv(os.path.join(DATA_PATH, "agents_raw.csv"))
tickets_df = pd.read_csv(os.path.join(DATA_PATH, "tickets_raw.csv"))
escalations_df = pd.read_csv(os.path.join(DATA_PATH, "escalations_raw.csv"))

for _, row in customers_df.iterrows():
    cur.execute("""
        INSERT INTO Customers(customer_id, first_name, last_name, email, phone, account_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (row['customer_id'], row['first_name'], row['last_name'], row['email'], row['phone'], row['account_type']))

for _, row in agents_df.iterrows():
    cur.execute("""
        INSERT INTO Agents(agent_id, first_name, last_name, email, role, is_active)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (row['agent_id'], row['first_name'], row['last_name'], row['email'], row['role'], row['is_active']))

for _, row in tickets_df.iterrows():
    cur.execute("""
        INSERT INTO Tickets(ticket_id, customer_id, agent_id, category, priority, status, created_at, first_response_at, resolved_at, escalated_flag, reopen_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['ticket_id'], row['customer_id'], row['agent_id'], row['category'], row['priority'],
        row['status'], row['created_at'], row['first_response_at'], row['resolved_at'],
        row['escalated_flag'], row['reopen_count']
    ))

for _, row in escalations_df.iterrows():
    cur.execute("""
        INSERT INTO Escalations(escalation_id, ticket_id, level, handled_by, escalation_date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        row['escalation_id'], row['ticket_id'], row['level'], row['handled_by'], row['escalation_date']
    ))

conn.commit()
conn.close()
print("All data successfully loaded into SQLite database!")
