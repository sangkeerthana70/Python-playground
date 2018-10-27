# In Python, you can also convert strings to integer and float values

price_cake = '15'
price_cookie = '6'

# String concatenation
total = price_cake + price_cookie
print("The total is: " + total + "$")

# Explicit type conversion to integer
total = int(price_cake) + int(price_cookie)
print("The total is: " + str(total)  + "$")