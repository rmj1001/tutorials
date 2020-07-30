# Try/Except is a way to catch errors
# in Python code. Because these errors
# will often stop your code, try/except
# will handle the error, instead of 
# stopping your code.

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")

# In this code, it will try to see if the code
# throws an error. If it doesn't, it moves on
# from the try/except code block. Otherwise,
# it runs the code in the except statement.

# Unfortunately, using just the except statement
# in a bare state, it will catch ANY error in the
# code. 

# To catch a specific error, create more than 1
# except block to catch each possible error.

# You can also store an error as a variable.
# Ex. except <error> as <var>:

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

# As a general "best practice", always
# use more than 1 except block to catch
# specific errors.