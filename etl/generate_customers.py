from faker import Faker 
import pandas as pd
import numpy as np

fake = Faker(locale='en_US')
Faker.seed(4321)

def generate_customers(num_customers):
    customers_list = []

    account_type = ["Standard", "Premium", "Enterprise"]
    account_probs = [0.45, 0.3, 0.25]

    for i in range(1, num_customers + 1):
        customer = {}
        customer['customer_id'] = i 
        customer['first_name'] = fake.first_name()
        customer['last_name'] = fake.last_name()
        customer['email'] = fake.email()
        customer['phone'] = fake.phone_number()
        customer['account_type'] = np.random.choice(account_type, p=account_probs)

        customers_list.append(customer)

    return pd.DataFrame(customers_list)

num_customers = 150
customers_df = generate_customers(num_customers)

customers_df.to_csv(r'C:\Users\juans\OneDrive\Documents\Programming Projects\support-tickets-analytics-sql\data\customers_raw.csv')

print(customers_df.head())