
import numpy as np

# Student marks
marks = np.array([
    [78, 85, 90, 72, 88],
    [65, 70, 75, 80, 69],
    [92, 88, 95, 90, 94],
    [55, 60, 58, 62, 65]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)
print("Data Type:", marks.dtype)

# Total marks of each student
totals = np.sum(marks, axis=1)

print("\nTotal marks of each student:")
print(totals)

# Average marks of each student
avg = np.mean(marks, axis=1)

print("\nAverage marks of each student:")
print(avg)

# Highest total score
high_score = np.max(totals)

print("\nHighest total score:", high_score)

# Top student
top_student = np.argmax(totals)

print("Top student index:", top_student)
print("Top student:", top_student + 1)

# Average of each subject
subject_avg = np.mean(marks, axis=0)

print("\nAverage of each subject:")
print(subject_avg)

# Pass / Fail
passed = avg >= 70

print("\nPassed students:")
print(passed)

# Marks of passing students
passing_marks = marks[passed]

print("\nMarks of passing students:")
print(passing_marks)
