## linear algebra   
import numpy as np
#DETERMINANT OF 2by2 matrix
A = np.array([[1, 2], [3, 4]])
print(np.linalg.det(A))
#ex 2
b=np.array([[5,2],
             [3,1]])
print(np.linalg.det(b))
##inverse of 2by2 matrix
A = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(A))
b=np.array([[5,2],
            [2,7]])
print(np.linalg.inv(b))