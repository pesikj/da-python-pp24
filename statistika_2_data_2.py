import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points (years of data)
n = 25

# Generate random values for the variables
# Rainfall in millimeters, Sunlight in hours per day, Temperature in Celsius, Soil moisture in percentage
rainfall = np.random.normal(1000, 200, n)  # Mean 1000 mm, Stddev 200 mm

# Generate avocado yield based on a simple regression formula
# Coefficients are arbitrary to simulate the effect of each variable
yield_kg = (0.25 * rainfall) + np.random.normal(0, 30, n)

# Introduce an outlier for the last entry by multiplying its value by 3
yield_kg[-2] = yield_kg[-2] * 5
yield_kg[-1] = yield_kg[-1] * 5

# Create a DataFrame
data = pd.DataFrame({
    'rainfall': rainfall,
    'avocado_yield': yield_kg
})

# Display the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file if needed
data.to_csv('avocado_farming_data_outlier.csv', index=False)
