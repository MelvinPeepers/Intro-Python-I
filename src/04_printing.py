"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# https://docs.python.org/3/library/stdtypes.html?highlight=printf#old-string-formatting
# https://www.geeksforgeeks.org/python-output-formatting/
print('x is %d, y is %f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
# https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
string_method = 'x is {0}, y is {1}, z is "{2}"'
print(string_method.format(x, y, z))


# Finally, print the same thing using an f-string
# https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
print(f"x is {x}, y is {y}, z is '{z}'")
