import numpy as np
from scipy import stats
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(42)

# Generate two lists of numbers, each with 20 values
list_1 = np.random.normal(loc=55, scale=5, size=20)  # List 1 with a mean of 50
list_2 = np.random.normal(loc=50, scale=5, size=20)  # List 2 with a slightly higher mean of 55

# Perform a one-sided t-test: testing if the mean of list_2 is greater than the mean of list_1
t_stat, p_value = stats.ttest_ind(list_1, list_2, alternative='greater')

# Adjust the means until the p-value is approximately 0.01
while p_value > 0.011 or p_value < 0.009:
    list_2 = np.random.normal(loc=np.mean(list_1) - np.random.uniform(3, 5), scale=5, size=20)
    t_stat, p_value = stats.ttest_ind(list_1, list_2, alternative='greater')

# Print the lists and p-value
print("List 1:", list_1)
print("List 2:", list_2)
print(f"One-sided p-value: {p_value:.4f}")

# Create a DataFrame to hold the data
data = pd.DataFrame({'Pripravek': list_1, 'Placebo': list_2})

# Save the DataFrame to a CSV file (without index)
data.to_csv('student_results.csv', index=False)
