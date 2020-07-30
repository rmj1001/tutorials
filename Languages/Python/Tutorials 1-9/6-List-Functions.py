lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

# Adds another list to the end of the list
friends.extend(lucky_numbers)
print(friends)

# Adds an element to the end of the list
friends.append("Creed")
print(friends)

# Adds an element to a specific spot in the list
friends.insert(1, "Kelly")
print(friends)

# Removes an element from the list
friends.remove("Jim")
print(friends)

# Takes the last element off of the list
friends.pop()

# Prints the element spot (index #) of the element name
print(friends.index("Oscar"))

# Sorts the list into alphebetical order
friends.sort()

# Prints the number of times an element shows up in a list
print(friends.count("Jim"))

# Reverses the order of the list
lucky_numbers.reverse()

# Copies a list into a new list
friends2 = friends.copy()

# Clears the friends list
friends.clear()