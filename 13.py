##deleting in array
#1d array
import numpy as np
arr = np.array([1,2,3,4,5,6])
new_arr = np.delete(arr, 0)
print(new_arr)
#2d array
arr_2d = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

new_arr_2d =np.delete(arr_2d,1,axis=0)
print(new_arr_2d)#will delete the second row of the 2d array
new_arr_2d =np.delete(arr_2d,1,axis=1)
print(new_arr_2d)#will delete the second column of the 2d array
