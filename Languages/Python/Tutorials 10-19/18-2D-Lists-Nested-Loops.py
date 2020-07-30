# If you want, you can make
# lists inside of lists, creating
# a 2D grid in a list. See below

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# You must call the original list first,
# then the row, then the column.
# Ex. print(list[row][column])

# Prints the element in row 0, column 0.
print(number_grid[0][0])

# If you want to nest for loops, put
# a for loop inside a for loop.
# See below.

# Prints each element in the rows separately
for row in number_grid:
    print(row)
    for col in row:
        print(col)

