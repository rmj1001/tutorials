# If statements check to see if a condition
# is true. If it's not, it will move on to
# the next if statement. Otherwise, it will
# run the code in the code block created by
# the if statement, then move on in the code.

# Reminder: to create a code block, indent on
# the next line. { } don't create code blocks
# in Python.

is_male = True
is_tall = True

# Checks to see if is_male is true
if is_male:
    print("You are a Male.")
else:
    print("You are not a Male.")

# If you wish to check for multiple
# Conditions in the if statement, use
# one of 2 keywords, "or" or "and"

# Checks to see if you are a Male, or Tall, or both.
if is_male or is_tall:
    print("You are a Male, or Tall, or both.")
else:
    print("You are neither Male or Tall.")

# Checks to see if you are tall AND male.
if is_male and is_tall:
    print("You are a Tall Male.")
else:
    print("You are neither tall, nor male.")

# If a statement is not true, you can use an "elif", 
# aka else if keyword to check for another condition,
# before defaulting to the else statement. 

# You will need to use not(condition) to state the 
# condition is false if you originally tested for both 
# conditions to be true.

if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
else:
    print("You are neither tall, nor male.")