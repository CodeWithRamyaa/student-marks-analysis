students = {
    "Anu": 85,
    "Ravi": 72,
    "Priya": 91,
    "Kiran": 64,
    "Sneha": 78
}

print("STUDENT MARKS ANALYSIS")

for name, marks in students.items():
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

    print(name, "| Marks:", marks, "| Grade:", grade)

average = sum(students.values()) / len(students)

print("Average marks:", average)
print("Highest marks:", max(students.values()))
print("Lowest marks:", min(students.values()))
