import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of data points (years of data)
n = 500

# Generate random values for the variables
# Rainfall in millimeters, Sunlight in hours per day, Temperature in Celsius, Soil moisture in percentage
rainfall = np.random.normal(1000, 200, n)  # Mean 1000 mm, Stddev 200 mm
sunlight = np.random.normal(8, 1, n)       # Mean 8 hours/day, Stddev 1 hour/day
soil_moisture = np.random.normal(50, 10, n) # Mean 50%, Stddev 10%
pests = np.random.randint(0, 20, n)        # Number of pest infestations (0 to 20)
regions = np.random.choice(['North', 'South', 'West'], size=n)

region_coefficients = {
    'North': -30,  # North has better conditions for avocado growth
    'South': 50, # South has harsher conditions, reducing yield
    'West': 20    # West has moderate conditions, slightly improving yield
}
region_effect = np.array([region_coefficients[region] for region in regions])

# Generate avocado yield based on a simple regression formula
# Coefficients are arbitrary to simulate the effect of each variable
yield_kg = (0.25 * rainfall) + (10 * sunlight) + (0.8 * soil_moisture)  - (5 * pests) + region_effect + np.random.normal(0, 30, n)

# Create a DataFrame
data = pd.DataFrame({
    'rainfall': rainfall,
    'sunlight': sunlight,
    'soil_moisture': soil_moisture,
    'pests': pests,
    'regions': regions,
    'avocado_yield': yield_kg
})

# Display the first few rows of the dataset
data.head()


data.to_csv('avocado_farming_data.csv', index=False)
