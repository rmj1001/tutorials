# To open a file, see example
# Ex. open("file.ext", "r | w | a | r+")
# r  - Read file
# w  - Write file
# a  - Append file
# r+ - Read and write file

# Open the file using a variable
employee_file = open("employees.txt", "r")

# To see if the file is readable, use
# var.readable()
print(employee_file.readable())

# var.readline() - reads the first line of the file,
# unless readline is called before that. Then it prints
# the next line.
employee_file.readline()
employee_file.readline()

# To read multiple files,
# use var.readlines()
print(employee_file.readlines)

# Or, print a specific line in the file
print(employee_file.readlines()[2])

# Prints all employees in a file (longhand)
for employee in employee_file.readlines():
    print(employee)

# To close a file, do
# var.close()
employee_file.close()