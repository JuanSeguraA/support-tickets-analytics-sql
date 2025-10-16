from faker import Faker
import pandas as pd
import numpy as np

fake = Faker(locale='en_US')
Faker.seed(4321)
np.random.seed(4321)

tickets_df = pd.read_csv(r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\tickets_raw.csv")
agents_df = pd.read_csv(r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\agents_raw.csv")

def generate_escalations(tickets_df, agents_df):
    escalations_list = []
    escalation_id = 1

    tickets = tickets_df.to_dict(orient='records')
    agents = agents_df['agent_id'].tolist()

    for ticket in tickets:
        if ticket['escalated_flag'] == 1:

            num_levels = np.random.randint(1, 4)
            for level in range(1, num_levels + 1):
                escalation = {}
                escalation['escalation_id'] = escalation_id
                escalation['ticket_id'] = ticket['ticket_id']
                escalation['level'] = level
                escalation['handled_by'] = np.random.choice(agents)

                created_at = pd.to_datetime(ticket['created_at'])
                resolved_at = pd.to_datetime(ticket['resolve_at']) if pd.notna(ticket['resolve_at']) else created_at + pd.Timedelta(days=7)
                escalation['escalation_date'] = fake.date_time_between(start_date=created_at, end_date=resolved_at)

                escalations_list.append(escalation)
                escalation_id += 1

    return pd.DataFrame(escalations_list)

escalations_df = generate_escalations(tickets_df, agents_df)

escalations_df.to_csv(r"C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\escalations_raw.csv", index=False)

print(escalations_df.head())
