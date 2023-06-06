
def main():
    sum = int()
    print("Amount Due: 50")
    while sum < 50:
        coin = int(input("Insert coin: "))
        #if (coin != 25) or (coin != 10) or (coin != 5):
        #    break
        sum += coin
        remainer = 50 - coin
        if remainer == 0:
            print("Change Owed: 0")
        else:
            print(f"Amount Due: {50 - sum}")
      

main()
