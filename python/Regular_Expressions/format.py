import re

# surname, name as input
name = input("What's your name? ".strip())
if matches := re.search(r"(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"helo, {name}")
