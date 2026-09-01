#prinr max  value in array
import numpy as np
arr=np.array([70,56,70,88,48])
print(np.max(arr))
#print index of max value
print(np.argmax(arr))
##EXAMPLE 2
names=np.array(["Ali","Sara","Ahmed","Zara"])
marks=np.array([70,90,60,80])
highest_marks=np.argmax(marks)
print(f"Student with highest marks: {names[highest_marks]}")
print(f"Highest marks: {marks[highest_marks]}")
