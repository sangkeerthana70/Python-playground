# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple",  "cherry", "banana"]
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        break