from cs50 import get_int

# Prompts user for a number
x = get_int("x: ")

# Prompts user for another number
y = get_int("y: ")

#Perform some math operation
print(f"{x} plus {y} is {x+ y}")
print(f"{x} minus {y} is {x - y}")
print(f"{x} times {y} is {x * y}")
print(f"{x} truly divided by {y} is {x / y}")
print(f"{x} floor-divided by {y} is {x // y}")
print(f"remainder of {x} divided by {y} is {x % y}")

