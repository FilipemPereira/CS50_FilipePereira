def calculation(mass):
    c: int = 300000000
    return mass * c**2

def main():
    mass = int(input("m:"))
    print(calculation(mass))

main()