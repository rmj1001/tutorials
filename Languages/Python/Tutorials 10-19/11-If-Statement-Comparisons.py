# In if statements, you might need to compare 2
# values or variables to each other, so you will need
# to use Comparison operators.

# Comparison operators:
# == is equal to (a single = assigns a variable.)
# != is not equal to.
# <= is less than or equal to.
# >= is greater than or equal to.
# < is less than.
# > is greater than.

def max_num(num1, num2, num3):

    # Checks to see if num1 is greater than or
    # equal to num 2 and 3.
    if num1 >= num2 and num1 >= num3:
        return num1
    
    # Checks to see if num2 is greater than or
    # equal to num 1 and 300
    elif num2 >= num1 and num2 >= num3:
        return num2

    # If neither of the above statements were true,
    # it returns num3.
    else:
        return num3

print(max_num(3, 4, 5))