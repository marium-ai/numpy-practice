##ARRANGE ARRAY IN ASCENDING ORDER
import numpy as np
arr = np.array([10,40,80,33,20,50,60,70])
sorted_arr = np.sort(arr)
print(sorted_arr)
#EXAMPLE 2
arr2=np.array([10,10,30,70,80,70,60,50,40,30,20,10])
new_arr2=np.unique(arr2)
sorted_arr2=np.sort(new_arr2)
print(sorted_arr2)
##ARRANGE ARRAY IN DESCENDING ORDER
sorted_arr3 = np.sort(arr)[::-1]
print(sorted_arr3)
sorted_arr4 = np.sort(arr2)[::-1]
print(sorted_arr4)