import csv

students = []
# with dictReader, he csv file can be modified anytime
# And if someone change our csv file ...
with open("students4.csv") as file:
    reader = csv.Dictreader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
