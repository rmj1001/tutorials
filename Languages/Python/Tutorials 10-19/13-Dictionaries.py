# Sometimes you want to use smaller words
# for bigger ones. In this tutorial, we will
# make a "dictionary", which defines new key
# values for Python.

# First, initialize a variable for the dictionary.
# Second, use this format:
#
# var = {
# "key1" = "definition1",
# "key2" = "definition2",
# "key3" = "definition3"
# }

# Note: You must put a comma at the end of
# a line in a dictionary if there is another
# entry below it.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "March": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Prints all dictionary definitions.
print(monthConversions)

# Prints the full definition of a specified key.
print(monthConversions["Jan"])

# Alternate way to print full definition of a specified key
print(monthConversions.get("Dec"))

# If you input a key that is not mappable to a value in
# the dictionary, it will return "None", unless you use 
# var.get("key"). Add another parameter to the function like
# this (var.get("key", "Error message")) to give your own error
# message.

print(monthConversions.get("Luv", "Not a valid Key."))

# Tip: You can use numbers as keys instead of strings.