students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Herry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# notion of set
""""
houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
"""
houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)