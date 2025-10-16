from faker import Faker 
from datetime import datetime
import pandas as pd
import numpy as np


fake = Faker(locale='en_US')
Faker.seed(4321)

def generate_tickets(num_tickets, customers_df, agents_df):
    tickets_list = []

    categories = ["Billing", "Technical", "Account", "Bug", "Feature"]
    category_probs = [0.2, 0.45, 0.15, 0.1, 0.1]

    priorities = ["Low", "Medium", "High", "Urgent"]
    priority_probs = [0.3, 0.45, 0.2, 0.05]

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 1, 1)

    for i in range(1, num_tickets + 1):
        ticket = {}

        ticket['ticket_id'] = i

        customer = customers_df.sample(1).iloc[0] # customer id
        agent = agents_df.sample(1).iloc[0] # agent id
        ticket['customer_id'] = customer.customer_id
        ticket['agent_id'] = agent.agent_id

        ticket['category'] = np.random.choice(categories, p=category_probs)
        ticket['priority'] = np.random.choice(priorities, p=priority_probs)

        ticket['created_at'] = fake.date_time_between(start_date=start_date, end_date=end_date)
        created_at = ticket['created_at']

        # Represent response times as logarithmically distributed as "Urgent" times will have faster responses with fewer longer responses (due to right-skew nature of humanb response time)
        priority_ln = {"Low": (3,0.5), "Medium": (2.7, 0.5), "High": (2.3, 0.5), "Urgent": (2, 0.5)}
        mu, sigma = priority_ln[ticket['priority']]
        first_response_minutes = pd.Timedelta(minutes=int(np.random.lognormal(mu, sigma)))  # Timedelta allows for arithmetic operations on datetime objects
        ticket['first_response_at'] = created_at + first_response_minutes

        # Normally distribute resolution times, with higher priority tickets having shorter resolutions than lower priority tickets
        if ticket['priority'] in ['High', 'Urgent']:
            resolve_hours = np.random.normal(loc=2, scale=0.5)
        else:
            resolve_hours = np.random.normal(loc=5, scale=2)

        # catch any negative values as a result of normal distribution 
        resolve_hours = max(0.5, resolve_hours)

        ticket['resolve_at'] = ticket['first_response_at'] + pd.Timedelta(hours=round(resolve_hours, 2))

        cutoff = pd.Timestamp("2024-11-01")
        ticket['status'] = "Closed" if ticket['resolve_at'] <= cutoff else "Open"

        escalation_base = 0.03
        if ticket['priority'] == "High":
            escalation_base += 0.06
        elif ticket['priority'] == "Urgent":
            escalation_base += 0.10
        if ticket['category'] in ["Technical", "Bug"]:
            escalation_base += 0.04
        if customer.account_type == "Enterprise":
            escalation_base += 0.05
        ticket['escalated_flag'] = int(np.random.rand() < escalation_base)


        if np.random.rand() < 0.9:
            ticket['reopen_count'] = 0
        else:
            ticket['reopen_count'] = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])

        tickets_list.append(ticket)

    return pd.DataFrame(tickets_list)


customers_df = pd.read_csv(r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\customers_raw.csv")
agents_df = pd.read_csv(r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\agents_raw.csv")

num_tickets = 1000
tickets_df = generate_tickets(1000, customers_df, agents_df)
tickets_df.to_csv(r'C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\tickets_raw.csv')

print(tickets_df.head())