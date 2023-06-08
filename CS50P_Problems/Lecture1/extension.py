"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name
ends, case-insensitively, in any of these suffixes:

images - gif, jpg, jpeg, png
application - pdf, zip
text/plain - txt

match equivalent to switch in c and other c based languages
"""

# find(<substring>) - return the index where occur the first occurrence of the substring

def extension(fileName) -> any:
    fileName = fileName.lower()
    for c in fileName:
        if c == ".":
            i = fileName.find(".")
    extension = fileName[i + 1:]

    match extension:
        case "gif" | "jpg" | "jpeg" | "png":
            print(f"image/{extension}")
        case "pdf" | "zip":
            print(f"application/{extension}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octed-stream")

def main():
    fileName = input("File name:")
    extension(fileName)

main()
