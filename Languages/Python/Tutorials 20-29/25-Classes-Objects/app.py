# Classes are ways to define 
# new types of data in Python.

# Import Student class from Student file
from Student import Student

# student1 is an object
student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)

student2 = Student("Pam", "Art", 2.5, True)

print(student2.gpa)