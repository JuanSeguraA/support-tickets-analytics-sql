from faker import Faker 
import pandas as pd
import numpy as np

fake = Faker(locale='en_US')
Faker.seed(4321)

def generate_agents(num_agents):
    agents_list = []

    agent_roles = ['Support', 'Senior Support', 'Team Lead', 'Manager']
    role_probs = [0.6, 0.3, 0.075, 0.025]

    is_active_probs = [0.9, 0.1]

    for i in range(1, num_agents + 1):
        agent = {}
        agent['agent_id'] = i
        agent['first_name'] = fake.first_name()
        agent['last_name'] = fake.last_name()
        agent['email'] = fake.email()
        agent['role'] = np.random.choice(agent_roles, p=role_probs)
        agent['is_active'] = np.random.choice([True, False], p=is_active_probs)

        agents_list.append(agent)

    return pd.DataFrame(agents_list)

num_agents = 20
agents_df = generate_agents(num_agents)

agents_df.to_csv(r'C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\agents_raw.csv')