def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            pass
            #print("x is not a integer")

main()