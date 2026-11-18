import csv

with open("C:/Users/maort/Desktop/Code-The-Dream/python-intro-homework/week-7/data/students.csv", 'r') as file:
    students = csv.DictReader(file)
    for student in students:
        print(f"{student['name']}: {student['score']}")
