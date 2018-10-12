from cs50 import get_int

#prompts user for a positive integer
while True:
    n = get_int("Positive number: ")
    if n > 0:
        break

# prints out this many rows
for i in range(n):

    # prints out this many columns
    for j in range(n):
        print("#", end="")
    print()