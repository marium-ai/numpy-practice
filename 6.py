#indexing
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])  # Access the first element
print(arr[2])  # Access the third element
print(arr[-1]) # Access the last element
#slicing
print(arr[1:4])  # Access elements from index 1 to 3 
print(arr[:4])  # Access elements from the start to index 3
print(arr[2:])  # Access elements from index 2 to the end
print(arr[::2])  # Access every second element
print(arr[::-1])  # Access elements in reverse order