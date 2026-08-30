import numpy as np

# Generate random values from a given array
arr = np.array([5, 10, 15, 20, 25, 30])

print(np.random.choice(arr))
print(np.random.choice(arr, 3))


# Generate a reproducible random sequence
np.random.seed(42)

print(np.random.randint(1, 100))
print(np.random.randint(1, 100))
print(np.random.randint(1, 100))