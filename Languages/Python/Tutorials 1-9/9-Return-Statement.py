# The return statement returns information
# from a function.

def cube(num):

    # Returns the cube of num.
    return num ** 3

    # No code will run after a return
    # keyword will run in a function

# Prints the returned value from the function
print(cube(3))

# assigns returned value from cube function
# to a variable
result = cube(4)

# Prints the variable, with the assigned
# return value from the function
print(result)