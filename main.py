import pandas as pd
import matplotlib.pyplot as plt
from utils import add_full_name, add_age_group, merge_data, \
    calculate_total_spending_by_age, export_visualize_spending
import multiprocessing


def parallelize_data_processing(data, function):
    # Split the data into chunks for parallel processing
    chunk_size = 1000
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    num_processes = multiprocessing.cpu_count()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Apply the function to each chunk in parallel
    results = pool.map(function, chunks)

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    # Combine the results from all chunks
    return pd.concat(results, ignore_index=True)


if __name__ == '__main__':

    # Load customer and purchase data
    customers = pd.read_csv('customers.csv')
    purchases = pd.read_csv('purchases.csv')

    # Define data processing functions
    data_processing_functions = [
        add_full_name,
        add_age_group,
    ]

    # Parallelize data processing for 'full_name' and 'age_group' columns
    for func in data_processing_functions:
        customers = parallelize_data_processing(customers, func)

    # Merge customer and purchase data
    merged_data = merge_data(customers, purchases)
    merged_data.to_csv("results/combined_data.csv")

    # Calculate total spending by age group
    spending_by_age = calculate_total_spending_by_age(merged_data)
    spending_by_age.to_csv("results/age_group_spending.csv")

    # Visualize spending by age group
    export_visualize_spending(spending_by_age)
    plt.savefig("results/total_spending_by_age_group.png")
