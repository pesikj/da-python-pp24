import numpy as np
import pandas as pd
from scipy import stats

# Set the desired parameters
mean = 50
std_dev = 5
size1 = 100
size2 = 100

data1 = np.random.normal(loc=mean, scale=std_dev, size=size1)
mean_adjust = mean + 0.1

# Function to adjust the second set to achieve the desired p-value
def generate_data_with_p_value(mean1, mean2, std, size1, size2, target_p):
    while True:
        # Generate the second set of numbers
        data2 = np.random.normal(loc=mean2, scale=std, size=size2)
        # Perform two-sided t-test
        t_stat, p_value = stats.ttest_ind(data1, data2, alternative='greater')
        print(p_value)
        if np.abs(p_value - target_p) < 0.001:  # Allowable tolerance for p-value
            return data1, data2, p_value
        # Adjust the mean for the next iteration
        if p_value < target_p:
            mean2 += 0.01  # Small increment to move towards the desired p-value
        else:
            mean2 -= 0.01

data1, data2, final_p_value = generate_data_with_p_value(mean, mean_adjust, std_dev, size1, size2, target_p=0.03)
df = pd.DataFrame({'Potion': np.concatenate([data1, [None]*size2]), 'Placebo': np.concatenate([[None]*size1, data2])})


#data1, data2, final_p_value = generate_data_with_p_value(mean, mean_adjust, std_dev, size1, size2, target_p=0.03)
#df = pd.DataFrame({'Skola 1': np.concatenate([data2, [None]*size2]), 'Skola 2': np.concatenate([[None]*size1, data2])})


# Save and display the dataframe

# Display the final p-value achieved
print(f"Final p-value: {final_p_value:.4f}")

df.to_csv("statistika-1-assets/skoly.csv", index=False)