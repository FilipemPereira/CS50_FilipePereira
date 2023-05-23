def mathInterpreter(input) -> str:
    # unpack teh list
    x, operator, y = input.split(" ")
    n1 = int(x)
    n2 = int(y)
    match operator:
        case "+":
            result = n1 + n2
        case "-":
            result = n1 - n2
        case "*":
            result = n1 * n2
        case "/":
            result = float(n1) / n2
        case _:
            result = "ERROR!"

    return result

def main():
    line = input("Expression: ")
    print(mathInterpreter(line))

main()