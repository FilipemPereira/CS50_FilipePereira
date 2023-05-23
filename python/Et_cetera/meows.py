
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meows")

def meow(n: int) -> str:
    """
    meow n times
 
    : param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow \n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")