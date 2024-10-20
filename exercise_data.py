import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(0)

# Number of data points
N = 100

# Generate Poverty Rate (PR) - in percentage (%)
mean_PR = 20  # Average poverty rate
std_PR = 5    # Standard deviation
PR = np.random.normal(mean_PR, std_PR, N)

# Generate Unemployment Rate (UR) - in percentage (%)
# UR depends on PR
beta_UR_PR = 0.5
std_UR = 2
UR = beta_UR_PR * PR + np.random.normal(0, std_UR, N)

# Generate Crime Rate (CR) - incidents per 100,000 people
# CR depends on both PR and UR
beta_CR_PR = 0.4
beta_CR_UR = 0.3
std_CR = 3
CR = beta_CR_PR * PR + beta_CR_UR * UR + np.random.normal(0, std_CR, N)

# Generate Education Level (EL) - average years of schooling
# EL inversely depends on PR and UR
beta_EL_PR = -0.5
beta_EL_UR = -0.7
base_EL = 12  # Base education level
std_EL = 1
EL = base_EL + beta_EL_PR * PR + beta_EL_UR * UR + np.random.normal(0, std_EL, N)

# Generate Median Age (MA) - in years
# Unrelated to other variables
mean_MA = 35  # Average median age
std_MA = 5
MA = np.random.normal(mean_MA, std_MA, N)

# Generate Average Household Size (AHS) - number of people
# Unrelated to other variables
mean_AHS = 2.5  # Average household size
std_AHS = 0.5
AHS = np.random.normal(mean_AHS, std_AHS, N)

# Create a DataFrame
data = pd.DataFrame({
    'Poverty_Rate (%)': PR,
    'Unemployment_Rate (%)': UR,
    'Crime_Rate (per 100k people)': CR,
    'Education_Level (years)': EL,
    'Median_Age (years)': MA,
    'Avg_Household_Size (people)': AHS
})

# Display the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('crime_education_dataset.csv', index=False)


print(data.corr())