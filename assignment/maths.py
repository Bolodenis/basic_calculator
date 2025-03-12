import sys

def sub(a, b):
    return a - b

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

while True:
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))  

        choice = int(input("Select your choice of operation: \n1 for Subtraction\n2 for Addition\n3 for Multiplication\n4 for Division\n5 to Exit\n"))

        if choice == 1:
            print("Result:", sub(number1, number2))
        elif choice == 2:
            print("Result:", add(number1, number2))
        elif choice == 3:
            print("Result:", mult(number1, number2))
        elif choice == 4:
            print("Result:", div(number1, number2))
        elif choice == 5:
            print("Exiting the program...")
            sys.exit()
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
