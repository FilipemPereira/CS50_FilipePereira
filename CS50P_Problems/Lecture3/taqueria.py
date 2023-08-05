import os

itens = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    sum = 0.0
    while True:
        while True:
            try:
                item = input("Item: ").title().rstrip().lstrip()
                if item in itens:
                    sum += itens[item]
                else:
                    break
            except (EOFError, KeyboardInterrupt):
                print()
                print(f"\nTotal: ${sum:.2f}")


main()
