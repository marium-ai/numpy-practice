import numpy as np
##broadcasting
#single array
arr=np.array([1,2,3])
result=arr+5
print(result)
#1d to 2d array 
matrix=np.array([[1,2,3],
                 [4,5,6]])
vector=np.array([7,8,9])    
result=matrix+vector
print(result)