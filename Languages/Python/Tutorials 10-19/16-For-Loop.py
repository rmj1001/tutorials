# For loops are a kind of loop used when
# you know how many times the loop 
# should iterate.

# To initialize a for loop, use this format:
# Ex.
# for <variable> in <collection>:
#   code...
#   code...

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]

# Prints all elemets in array "friends",
# then loop stops
for friend in friends:
    print(friend)

# Prints all numbers from 0 to 10
for index in range(10):
    print(index)

# Prints all numbers from 3 to 10
for index in range(3, 10):
    print(index)

# Loops for every friend in the array
for index in range(len(friends)):
    print(index)

for index in range(5):
    if index == 0:
        print("First Iteration.")
    else:
        print("Not first.")

