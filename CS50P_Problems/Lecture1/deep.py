def TheGreatQuestion(answer) -> str: 
    check = str()
    if answer ==  "42" or answer.lower() == "forty two" or answer.lower() == "forty-two":
        check = "Yes"
    else:
        check = "No"
    return check

def main():
    answer = input("What is the Great Question of Life, the Universe and Everything?")
    print(TheGreatQuestion(answer))

main()
    
