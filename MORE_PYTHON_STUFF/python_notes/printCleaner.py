#!/usr/bin/python3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here's a quick tip that will help make your Python code way more
# efficient if you're not already taking advantage of it. If you want to
# print all the values in a list separated by a comma, there are a couple
# different ways you can go about doing this: there are complicated ways,
# and then there's an easy way. Here's an example of a complicated way:

food = ["pizza", "tacos", "ice cream", "cupcakes", "burgers"]
print(', '.join(str(x) for x in food))

# The output of the code above would be:

# pizza, tacos, ice cream, cupcakes, burgers

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The code inside of the print statement is not exactly concise and
# efficient. If you want to print all the values in the same list the
# easy, simple, and efficient way, try doing this with the print
# statement:

print(*food, sep=", ")

# The output of the print statement above would be exactly the same as
# the output in the first example:

# pizza, tacos, ice cream, cupcakes, burgers

# Printing lists this way will make sure your code looks clean and
# performs as efficiently as possible.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (for next examples)

abc = "ABC!"
defg = 42

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Example: format()

print("abc: {}, defg: {}".format(abc,defg))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Example: f-strings (Python 3.6+)

print(f"abc: {abc}, defg: {defg}")

