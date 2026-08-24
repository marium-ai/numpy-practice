import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)
new_array=np.insert(arr,3,100)
print(new_array)
arr2=np.delete(arr,3)
print(arr2)
#2d array
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
new_array_2d=np.insert(arr_2d,0,[5,6,7],axis=1)
print(new_array_2d)