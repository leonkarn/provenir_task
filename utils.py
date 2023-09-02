import pandas as pd
import matplotlib.pyplot as plt


def add_full_name(customers):
    # Add a 'full_name' column by combining 'first_name' and 'last_name'
    customers["full_name"] = customers["first_name"] + customers["last_name"]
    return customers


def add_age_group(customers):
    # Categorize customers into age groups and add an 'age_group' column
    customers['age_group'] = customers['age'].apply(
        lambda age: 'Young' if 18 <= age <= 30 else ('Middle-aged' if 31 <= age <= 45 else 'Senior'))
    return customers


def merge_data(customers, purchases):
    # Merge customer and purchase data on 'customer_id' column
    return pd.merge(purchases, customers, on='customer_id', how='inner')


def calculate_total_spending_by_age(df):
    # Calculate total spending by age group
    return df.groupby("age_group")["price"].sum().reset_index()


def export_visualize_spending(df):
    # Create a bar chart to visualize total spending by age group
    plt.figure(figsize=(8, 6))
    plt.bar(df['age_group'], df['price'], color='skyblue')
    plt.xlabel('Age Group')
    plt.ylabel('Total Spending')
    plt.title('Total Spending by Age Group')
    plt.xticks(rotation=45)
    plt.tight_layout()




