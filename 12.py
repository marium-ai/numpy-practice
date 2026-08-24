#concatenate array
import numpy as np

arr1 = np.array([1, 2])
arr2 = np.array([5, 6])
result = np.concatenate((arr1, arr2), axis=0)
print(result)
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6],[7, 8]])
result2 = np.concatenate((arr3, arr4), axis=1)
print(result2)