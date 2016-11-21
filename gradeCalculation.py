lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

""" Combining 3 dictionaries; lloyd, alice and tyler"""
students = [lloyd, alice, tyler]

for student in students:
    print(student["name"])
    print(student["homework"])
    print(student["quizzes"])
    print(student["tests"])
    print()

""" Calculating grades for students """


def average(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests


print("Lloyd's weighted average grade is %0.2f" % get_average(lloyd))
print("Alice's weighted average grade is %0.2f" % get_average(alice))
print("Tyler's weighted average grade is %0.2f" % get_average(tyler))

""" Assign a letter grade """


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print()
print("Lloyd: %0.2f %s" % (get_average(lloyd), get_letter_grade(get_average(lloyd))))
print("Alice: %0.2f %s" % (get_average(alice), get_letter_grade(get_average(alice))))
print("Tyler: %0.2f %s" % (get_average(tyler), get_letter_grade(get_average(tyler))))

""" Class average """


def get_class_average(students):
    results = []
    for student in students:
        result = get_average(student)
        results.append(result)
    avg = average(results)
    return avg


print("Class Average: %0.2f" % get_class_average(students))

""" Comparison if the class did well """

print("Class Letter: %s" % get_letter_grade(get_class_average(students)))