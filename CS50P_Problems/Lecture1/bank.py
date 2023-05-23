def greeting(salutation):
    salutation = salutation.lower()
    if salutation.startswith("hello"):
        salutation = "$0"
    elif salutation[0] == 'h' and salutation != "hello":
        salutation = "$20"
    else:
        salutation = "$100"
    return salutation

def main():
    salutation = input("Greeting: ")
    print(greeting(salutation))

main()