# Technical Challenge for Data Engineer Role


## Solution
To run this either use Docker in this way. After having installed it simply run the command below to build and run the image
~~~
docker-compose build && docker-compose up
~~~

Or alternatively if you have installed python , just run
~~~
pip install -r requirements.txt
~~~
to install the depedencies and after
~~~
python main.py
~~~
To run the script

The results are saved in results folder

## Overview

In this challenge, you will be provided with two datasets, `customers.csv` and `purchases.csv`. Your primary task is to process, transform, and analyze these datasets using your choice of tools and languages. While Python, Pandas, and other relevant libraries are suggested, you're free to use any stack you're comfortable with. The goal is to extract meaningful insights and produce a visualization that showcases the spending habits of different age groups.

## Requirements:

### Virtual Environment

Before starting, set up a virtual environment to manage the dependencies for this project. This ensures that the required packages don't interfere with other projects or system-wide installations. If you're unfamiliar with creating virtual environments, you can use tools like `venv` or `virtualenv`. Once set up, activate the virtual environment for all operations related to this challenge.

```bash
# Using venv (Python 3.3 and above)
python -m venv myenv
# On Windows
.\myenv\Scripts activate
# On macOS and Linux
source myenv/bin/activate
```

### Dependencies

- Install the required libraries for your chosen stack. If you opt for Python, you can install the commonly used libraries using `pip`:

    ```bash
    pip install pandas numpy matplotlib
    ```

### Data Files

Ensure you have the `customers.csv` and `purchases.csv` files available. These can be found [link to S3 or other hosting].

### Output Files

After executing the solution script, generate two CSV files (`combined_data.csv` and `age_group_spending.csv`) and one PNG file for the visualization (`total_spending_by_age_group.png`).

### Performance

Pay attention to the performance, especially when dealing with large datasets. If you're using Python, consider leveraging the `multiprocessing` module to enhance computational speed by leveraging multiple cores/processors.

### Documentation

Include inline comments where necessary to explain your code. Provide a brief documentation or README detailing how to execute the script, any assumptions made, and observations from the results.

### Quality and Testing

Aim to produce production-quality code. This means your code should be clean, maintainable, and robust. Accompany your solution with unit tests to ensure its correctness and reliability. Treat this as if you're submitting a feature to be deployed in a live environment.

### Submission

Submit the final code, preferably as a repository with a clear structure. This should include your main script or notebook, output CSV files, the visualization, and any accompanying tests. A README explaining your approach, tool choices, project hierarchy, and instructions to run the code will be highly appreciated.

### Hints

- **Functionality**: Ensure your code executes without errors and addresses all tasks mentioned in the challenge. Check that the correct output files are generated as specified.
- **Code Quality**: Organize your code into modular functions with proper naming conventions. Optimize your code, and if possible, leverage multiprocessing for faster processing.
- **Documentation & Clarity**: Add meaningful inline comments to explain complex parts of your code. Provide a clear README that outlines your approach and instructions to run the code.
- **Performance**: Implement effective multiprocessing to handle large datasets efficiently. Address potential bottlenecks and focus on optimizing execution time.
- **Analysis & Visualization**: Compute accurate insights from the data and create a well-labeled, visually appealing bar chart that presents the total spending by age group.
- **Project Directory Hierarchy**: Structure your project directory with a clear hierarchy. This can include separate folders for data, code, tests, and outputs.

## Tasks:

1. **Load the Data**: Import the datasets.
2. **Data Transformation**: Generate a `full_name` column by combining `first_name` and `last_name`. Categorize customers into age groups: `Young` (18-30), `Middle-aged` (30-45), and `Senior` (45+).
3. **Join Operation**: Merge the customers and purchases datasets on the `customer_id`. Ensure no data is lost in this operation.
4. **Analysis**: Compute the total spending for each age group.
5. **Visualization**: Create a bar chart to showcase the total spending by age group.
6. **Output**: Save the transformed and merged data into a new CSV file named `combined_data.csv`. Save the total spending by age group into another CSV file named `age_group_spending.csv`. Save your visualization as a PNG file.

Good luck!