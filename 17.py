import numpy as np
arr=np.array([1,2,np.nan,4,5,np.nan,6])
print(arr)
print(np.isnan(arr))
print(np.nanmean(arr))
arr2=np.nan_to_num(arr,nan=3)
print(arr2)
#is infinite
arr3=np.array([1,2,np.inf,4,np.inf,6])
print(np.isinf(arr3))