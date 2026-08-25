##spliting
import numpy as np
#1d array
arr=np.array([10,20,30,40,50,60])
print(np.split(arr,2))
#2d array
arr_2d=np.array([[1,2,3],
                 [4,5,6]])
new_arr_2d=np.split(arr_2d,3,axis=1)
print(new_arr_2d)