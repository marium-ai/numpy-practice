#stacking
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[4, 5], [6, 7]])
stacked_arr = np.stack((arr1, arr2), axis=1)
print(stacked_arr)
vstacked_arr = np.vstack((arr1, arr2))
print(vstacked_arr)
hstacked_arr = np.hstack((arr1, arr2))
print(hstacked_arr)