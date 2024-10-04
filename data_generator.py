import random
import pandas as pd

# Define constants
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]
salesmen = ["Alice", "Bob", "Charlie"]
products = ["DataFrame", "DataPipeline", "DataLake", "DataWarehouse", "DataModel"]

# Function to generate a random sales record
def generate_sales_record():
    # Randomly select 2 to 3 unique products for the salesman
    selected_products = random.sample(products, random.randint(2, 3))
    # Generate a random number of sales for each product
    product_sales = [f"{product}({random.randint(10, 100)})" for product in selected_products]
    # Combine product names and sales count into a single string
    return "; ".join(product_sales)

# Create an empty list to store data
data = []

# Populate the dataset
for month in months:
    for salesman in salesmen:
        sales_record = generate_sales_record()
        # Append data for each month and salesman
        data.append([month, salesman, sales_record])

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=["Month", "Salesman", "Product Sales"])

# Save the dataset as a TSV file
df.to_csv("sales_data.tsv", sep="\t", index=False)

