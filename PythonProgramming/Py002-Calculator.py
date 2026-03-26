# Simple Python calculator

print("Welcome to python build calculator!")

# Performs calculation based on operator
def calculate(a, operate, b):
    if operate == "+":
        return a + b
    elif operate == "-":
        return a - b
    elif operate == "*":
        return a * b
    elif operate == "/":
        return a / b
    else:
        return "Wrong Operation Input"


# Initial input
num1 = float(input("Enter the first number : \n"))

# Continuous calculation loop
while True:
    operation = input("Enter the operation (+,-,*,/) : \n")
    num2 = float(input("Enter the second number : \n"))

    result = calculate(num1, operation, num2)
    print(f"result : {result}")

    # Check if user wants to continue
    again = input("Do you wish to continue with the result (y/n) : \n").lower()

    if again == "y":
        num1 = result
    else:
        print("Goodbye!")
        break
