import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr)
new_arr = np.append(arr, [[10, 11, 12]], axis=None)

print(new_arr)