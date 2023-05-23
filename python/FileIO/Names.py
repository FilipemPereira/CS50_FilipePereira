"""
with open("names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
"""
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse = False):
    print(f"hello, {name}")
