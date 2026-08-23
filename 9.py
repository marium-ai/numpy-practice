#RESHAPING
import numpy as np
arr=np.array([1,2,3,4,5,6])
reshaped_array=arr.reshape(3,2)
print(reshaped_array)
#flattening ravel array
print(reshaped_array.flatten())
print(reshaped_array.ravel())
