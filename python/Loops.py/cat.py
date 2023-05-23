"""""
i = 3 
while i != 0:
    print("meow")
    i = i - 1
"""""
"""""
# if i is in list the loop will work
    
for _ in range(3):
    print("meow")

# repeat 3 times the string
print("meow\n" * 3, end="")

"""""
            
def main():
    number = get_number()
    meow(number)
        
def get_number():
    while True:
        n = int(input("What's n? "))
        if n < 0:
            continue
        else:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

