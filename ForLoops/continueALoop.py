# With the continue statement we can stop the current iteration of the loop, and continue with the next

fruits = ["apple", "banana", "cherry", "kiwi", "mangoes"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

