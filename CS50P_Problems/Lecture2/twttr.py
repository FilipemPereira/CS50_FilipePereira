def is_vowel(letter):
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False

def main():
    string = input("Input: ")
    output = ""
    for s in string:
        if is_vowel(s):
            output += ''
        else:
            output += s
    print("Output:", output)

main()