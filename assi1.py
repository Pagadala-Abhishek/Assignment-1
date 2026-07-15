import math

# Functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error! Square root of a negative number is not possible."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Factorial of a negative number is not possible."
    return math.factorial(int(a))


# Menu
while True:
    print("\n*** CALCULATOR ***")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Result =", addition(a, b))

    elif choice == 2:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Result =", subtraction(a, b))

    elif choice == 3:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Result =", multiplication(a, b))

    elif choice == 4:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Result =", division(a, b))

    elif choice == 5:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        print("Result =", modulus(a, b))

    elif choice == 6:
        a = float(input("Enter Base Number: "))
        b = float(input("Enter Power: "))
        print("Result =", power(a, b))

    elif choice == 7:
        a = float(input("Enter Number: "))
        print("Result =", square(a))

    elif choice == 8:
        a = float(input("Enter Number: "))
        print("Result =", square_root(a))

    elif choice == 9:
        a = int(input("Enter Number: "))
        print("Result =", factorial(a))

    elif choice == 10:
        print("Thank You! Exiting Calculator...")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 10.")
