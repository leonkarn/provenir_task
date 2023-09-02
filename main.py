from utils import *

if __name__ == '__main__':
    # Input file paths
    customers_file = 'customers.csv'
    purchases_file = 'purchases.csv'

    # Load data from CSV files
    customers = pd.read_csv(customers_file)
    purchases = pd.read_csv(purchases_file)

    # Add a 'full_name' column
    customers = add_full_name(customers)

    # Add an 'age_group' column
    customers = add_age_group(customers)

    # Merge customer and purchase data
    merged_data = merge_data(customers, purchases)
    merged_data.to_csv("combined_data.csv")

    # Calculate total spending by age group
    spending_by_age = calculate_total_spending_by_age(merged_data)
    spending_by_age.to_csv("age_group_spending.csv")

    # Visualize spending by age group
    export_visualize_spending(spending_by_age)
    plt.savefig("total_spending_by_age_group.png")
