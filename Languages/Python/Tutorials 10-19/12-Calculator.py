# Initialize variables
num1 = float(input("Enter first number\n\n>> "))
op = input("\nEnter operator\n\n>> ")
num2 = float(input("\nEnter second number\n\n>> "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Error! Invalid operation!")