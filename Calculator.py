import math
def addition():
    print("\n+================================+")
    print("|            Addition            |")
    print("+================================+")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    result = a + b
    print(f"Result: {result}")
def subtraction():
    print("\n+================================+")
    print("|           Subtraction          |")
    print("+================================+")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    result = a - b
    print(f"Result: {result}")
def multiplication():
    print("\n+================================+")
    print("|          Multiplication        |")
    print("+================================+")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    result = a * b
    print(f"Result: {result}")
def division():
    print("\n+================================+")
    print("|             Division            |")
    print("+================================+")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if b == 0:
        print("Cannot Divide By Zero!")
    else:
        result = a / b
        print(f"Result: {result}")
def modulus():
    print("\n+================================+")
    print("|             Modulus             |")
    print("+================================+")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    if b == 0:
        print("Cannot Divide By Zero!")
    else:
        result = a % b
        print(f"Result: {result}")
def power():
    print("\n+================================+")
    print("|              Power              |")
    print("+================================+")
    a = float(input("Enter Base Number: "))
    b = float(input("Enter Power: "))
    result = a ** b
    print(f"Result: {result}")
def square_root():
    print("\n+================================+")
    print("|           Square Root           |")
    print("+================================+")
    number = float(input("Enter Number: "))
    if number < 0:
        print("Cannot Find Square Root of a Negative Number!")
    else:
        result = math.sqrt(number)
        print(f"Square Root: {result}")
while True:
    print("\n+================================+")
    print("|          Calculator App        |")
    print("+================================+")
    print("|  1. Addition                   |")
    print("|  2. Subtraction                |")
    print("|  3. Multiplication             |")
    print("|  4. Division                   |")
    print("|  5. Modulus                    |")
    print("|  6. Power                      |")
    print("|  7. Square Root                |")
    print("|  8. Exit                       |")
    print("+================================+")
    try:
        choice = int(
            input("Choose an Option From 1 To 8: ")
        )
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            modulus()
        elif choice == 6:
            power()
        elif choice == 7:
            square_root()
        elif choice == 8:
            print("\n+================================+")
            print("|       Exited Successfully      |")
            print("+================================+")
            break
        else:
            print("Invalid Choice!")
            print("Please Choose Correct Choice!")
    except ValueError:
        print("Please Enter Valid Numbers!")