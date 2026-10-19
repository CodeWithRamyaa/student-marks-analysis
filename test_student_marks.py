import pandas as pd

def calculate_average(marks):
    return sum(marks) / len(marks)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

# Test 1: Average calculation
assert calculate_average([80, 70, 90]) == 80

# Test 2: Grade classification
assert get_grade(85) == "A"
assert get_grade(70) == "B"
assert get_grade(50) == "C"
assert get_grade(30) == "F"

# Test 3: Student data
students = {
    "Anu": [85, 88, 80],
    "Ravi": [72, 75, 68]
}

assert calculate_average(students["Anu"]) == 253 / 3
assert get_grade(72) == "B"

print("All tests passed successfully!")
