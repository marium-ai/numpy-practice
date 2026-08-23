import numpy as np
#rowa nd column
arr_2d = np.array([[1,2,3],
                    [4,5,6],
                     [6,7,8]])
print(arr_2d.shape)
#element of array
arr=np.array([[1,2,3],[4,5,6]])
print(arr.size)
# #no of dimensions
arr1=np.array([1,2,3])
arr2=np.array([[1,2,3],[4,5,6]])
arr3=np.array([[[1,2,3],[4,5,6]],
               [[7,8,9],[10,11,12]]])
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
#type changing
arr4=np.array([1.2,2.3,3.4])
int_arr=arr4.astype(int)
print(int_arr)
print(int_arr.dtype)