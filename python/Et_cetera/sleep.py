def main():
    n = int(input("What's n? "))
    for s in sheep:
        print(s)

# yield gera uma enorme quantidade de informação passo a passo
def sheep(n):
    flock = []
    for i in range(n):
        yield ("🐑️" * i)

if __name__ == "__main__":
    main()