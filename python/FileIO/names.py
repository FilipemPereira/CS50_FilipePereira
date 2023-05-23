""""
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

# sorted in alphabetic order
for name in sorted(names):
    printf(f"Hello, {name}")

name = input("What's your name? ")

# we run more that once
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""
# close the stream for us after line 22
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")