def replace(phrase):
    # replace - replace a substring for another in the original str object
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return phrase

def main():
    phrase = input()
    print(replace(phrase))

main()