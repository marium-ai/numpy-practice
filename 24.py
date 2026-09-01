import numpy as np
arr = np.array([5, 20,10,15])
print(arr)
print(np.argsort(arr))
#ex 2
students = np.array(["Ali", "Sara", "Ahmed", "Zara"])
marks = np.array([70, 90, 60, 80])
order = np.argsort(marks)
print(students[order])
print(marks[order])
#ex 3
arr2 = np.array([10, 20, 30, 40, 50])
indices = np.argsort(arr2)
print(indices)