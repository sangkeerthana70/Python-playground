#linear search

import sys
from cs50 import get_string

#Names in a phone book
book = [
    "Chen",
    "Chang",
    "Lee",
    "Louis",
    "Malary",
    "Muller",
    "Sheller",
    "Shiela",
    "Smith"]

# prompt user for a name
name = get_string("Name: ")
if name in book:
    print(f"Calling {name}")

else:
    print("Quitting")
