def main():
    yell("This", "is", "cs50")

def yell(*words):
    #print(phrase.upper())

    #upper = [word.upper() for word in words]
    
    # the function .upper can't be called
    uppercase = map(str.upper, words)
    print(*uppercase)

if __name__ == "__main__":
    main()