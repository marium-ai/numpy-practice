#printminimum value in an array
import numpy as np
arr=np.array([70,56,70,88,48])
print(np.min(arr))
print(np.argmin(arr))
#example 2
names=np.array(["Ali","Sara","Ahmed","Zara"])
marks=np.array([70,90,60,80])
lowest_marks=np.argmin(marks)
print(f"Student with lowest marks: {names[lowest_marks]}")
print(f"Lowest marks: {marks[lowest_marks]}")