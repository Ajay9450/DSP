import numpy as np

# Given parameters
S0 = 100
mu = 0.50
sigma = 0.5
dt = 0.01
num_paths = 1000
num_steps = 100

# Task 1: Array Creation (1 Mark)
np.random.seed(42)
Z = np.random.normal(0, 1, (num_paths, num_steps))

# Task 2: Array Manipulation (1 Mark)
# Calculate the step-by-step exponential multipliers
multipliers = np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

# Prepend a column of 1s to align with S0 during cumprod
multipliers_with_start = np.hstack([np.ones((num_paths, 1)), multipliers])

# Calculate trajectories
S = S0 * np.cumprod(multipliers_with_start, axis=1)

# Task 3: Basic Statistics & Slicing (2 Marks)
final_prices = S[:, -1] # Slice the last column
mean_final = np.mean(final_prices)
std_final = np.std(final_prices)

print(f"Mean of final prices: {mean_final:.2f}")
print(f"Std Dev of final prices: {std_final:.2f}")

# Task 4: Advanced Indexing (2 Marks)
# Get the indices that would sort the final prices
sorted_indices = np.argsort(final_prices)

# Use integer array indexing to extract full rows
bottom_5_paths = S[sorted_indices[:5]]
top_5_paths = S[sorted_indices[-5:]]

# print out mean and std of the two arrays
print("mean and standard deviation of bottom 5% ...")
print(bottom_5_paths.mean(), bottom_5_paths.std())
print("mean and standard deviation of top 5% ...")
print(top_5_paths.mean(), top_5_paths.std())
