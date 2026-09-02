import numpy as np
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

print(np.linalg.solve(A, b))
#ex 2
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
print(np.linalg.solve(A, b))
import numpy as np

a = np.array([1, 2, 3])

b = a

b[0] = 100

print(a)
print(b)