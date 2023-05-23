#import random
from random import choice

coin = choice(["heads", "tails"])
number = random.randint(1, 10)
cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(coin)
for card in cards:
    print(card)