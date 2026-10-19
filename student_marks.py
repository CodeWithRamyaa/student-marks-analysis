students = {
    "Anu": 85,
    "Ravi": 72,
    "Priya": 91,
    "Kiran": 64,
    "Sneha": 78
}

print("STUDENT MARKS ANALYSIS")
print("----------------------")

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

print("----------------------")
print("Average marks:", average)
print("Highest marks:", max(students.values()))
print("Lowest marks:", min(students.values()))
