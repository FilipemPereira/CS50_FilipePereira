import re

email = input("What's your mail?").strip()

""""
if  re.search(r"^[^@]+@[^@]+\.edu$ ", email):
    print("valid")
else:
    print("Invalid")
"""
# re.search(r"^\w+@\w\.edu$", email)
if  re.search(r"^[a-<A-Z0-9_]+@[a-<A-Z0-9_]+\.(edu|com)$ ", email):
    print("valid")
else:
    print("Invalid")