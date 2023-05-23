
students = {
    "Hermione": "Griffindor", 
    "Harry": "Griffindor",
    "Ron": "Griffindor",
    "Draco": "Slytherin"    
}
    
print(students)
print(students["Hermione"])
print(students["Draco"])

for student in students:
    print(student, students[student], sep =", ")