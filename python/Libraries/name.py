import sys
"""
try:
    print("hello , my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else: 
    print("hello, my name is", sys.argv[1])