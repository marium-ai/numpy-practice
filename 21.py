#print values based on condition
import numpy as np
marks= np.array([90, 80, 70, 60, 50,30])

result= np.where(marks>40, "Pass", "Fail")
print(result)

marks = np.array([35, 45, 67, 20, 89, 40])
result = np.where(marks>=50, "Pass", "Fail")
print(result)
#remove duplicate vlaues & print unique values
arr = np.array([1, 2, 3, 4, 5, 1, 2, 3])

unique_values = np.unique(arr)
print(unique_values)
arr = np.array([5, 5, 10, 10, 10, 20, 20, 30])

values, counts = np.unique(arr, return_counts=True)

print(values)
print(counts)