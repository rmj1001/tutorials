
# If you want to add data to a file,
# you can append the file.

employee_file = open("employees.txt", "a")
employee_file.write("\nNew line: \"Toby - Human Resources\"")
employee_file.close()

# To append data on a new line in a file,
# put the escape sequence \n before the 
# appended data.

employee_file = open("employees.txt", "a")
employee_file.write("\nNew Line: \"Kelly - Customer Service\"")
employee_file.close()

# If you want to override (over-write)
# a file, or write a new file, use this
# template:
# var = open("filename.ext", "w")

employee_file = open("employees2.txt", "w")
employee_file.write("Kelly - Customer Service")
employee_file.close()