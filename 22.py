# Find unique values and their counts
import numpy as np
arr = np.array([5, 5, 10, 10, 10, 20, 20, 30])

values, counts = np.unique(arr, return_counts=True)

print(values)
print(counts)
#EXAMPLE 2
grades=np.array(["A","B","C","A","B","C","A","D","E","F","A","B","C","A","B","C","A","D","E","F"])
counts = np.unique(grades, return_counts=True)
print(counts)