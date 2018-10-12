# prints any number of question marks specified by the user

from cs50 import get_int

n = get_int("Number: ")
for i in range(n):
    print('?', end = "\n")
print()