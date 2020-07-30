# A function is a group of code to
# perform a specific task.

# To initialize a function, use this template:
# def var():
#   code here...
#   code here...
# def var2():
#   code here...
#   code here...
#
# Note: To create a code block, you must indent from
# the statement running the code. 4 spaces or a tab 
# is used to indent.

# Another Note: if the function uses 2 or more words, 
# separate them with an underscore
# Ex. var_name

def say_hi():
    print("Hello User")

# To use (call) your function, type var() on a new line, 
# unindented from previous code

print("Top")

# Called function "say_hi"
say_hi()

print("Bottom")

# If you wish to use parameters in the function,
# put each parameter name in the parantheses,
# separated by a comma.
# Ex. def var_name(param1, param2, param3, etc...)
def say_hi2(name, age):
    print("Hello, "+name+"! You are "+age+".")

# Will call the function, using all parameters (name and age)
# Result: Hello, Mike! You are 35.
say_hi2("Mike", "35")