def is_camel_case(variable):
    for l in variable:
        if l.isupper():
            return True
    return False

def snake_case(variable)->str:
    string = ""
    if is_camel_case(variable):
        for l in variable:
            if l.isupper():
                string += "_" + l.lower()
            else:
                string += l
    else:
        print("Variable name not in camel case")
    return string

def main():
    variable = input("camelCase:")
    print(snake_case(variable))

main()