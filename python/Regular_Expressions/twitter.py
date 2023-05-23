import re

url = input("url: ").strip()

# now we have 2 groups
matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", "", url, re.IGNORECASE)

if matches:
    print(f"Username: ", matches.group(1))