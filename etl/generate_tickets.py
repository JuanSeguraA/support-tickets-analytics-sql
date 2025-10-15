from faker import Faker 
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

    start_date = pd.Timestamp("2024-01-01")



    for i in range(1, num_tickets + 1):
        ticket = {}

        ticket['ticket_id'] = i

        customer = customers_df.sample(1).iloc[0] # customer id
        agent = agents_df.sample(1).iloc[0] # agent id
        ticket['customer_id'] = customer.customer_id
        ticket['agent_id'] = agent.agent_id

        ticket['category'] = np.random.choice(categories, p=category_probs)
        ticket['priority'] = np.random.choice(priorities, p=priority_probs)

    

        ticket['created_at'] = fake.date_time_between(start_date="2024-01-01", end_date="2025-01-01")
