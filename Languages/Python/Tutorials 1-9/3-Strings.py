# To add a new line in a string, use escape sequence \n
# To add a " or ', do \" or \'
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

phrase = "Giraffe Academy"

# var.lower() makes the string lower
print(phrase.lower())

# var.islower() checks to see if the string is all lowercase
# returns a boolean value as a result
print(phrase.islower())

# var.lower().islower() makes the string all lower case, then
# checks to see if the string is lower case
print(phrase.lower().islower())

# var.upper() makes the string all uppercase.
print(phrase.upper())

# var.isupper() checks to see if the string is lower case.
# returns a boolean value as a result
print(phrase.isupper())

# var.upper().isupper() makes the string all upper case, then
# checks to see if the string is upper case
print(phrase.upper().isupper())

print(phrase[0])