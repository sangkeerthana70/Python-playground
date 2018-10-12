# prints any number of question marks specified by the user

from cs50 import get_int

#prompts user for a positive integer
while True:
    n = get_int("Positive number: ")
    if n >= 1:
        break

# prints how n number of  bricks
for i in range(n):
    print("#")