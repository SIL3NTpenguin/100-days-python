import art
import os

def add(n1, n2):
    """
    Adds two values together and returns the value.
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Subtracts the second value from the first and returns the value.
    """
    return n1 - n2

def multiply(n1, n2):
    """
    Multiplies two values together and returns the value.
    """
    return n1 * n2

def divide(n1, n2):
    """
    Divides the first value by the second and returns the value.
    """
    return n1 / n2

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def req_operator():
    operator = input("Pick an operation: ")
    if operator in operations.keys():
        return operator
    else:
        print("Invalid input! Acceptable operations:")
        for symbol in operations.keys():
            print(symbol)
        req_operator()

def calculator():
    print(art.logo)
    same_cal = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations.keys():
        print(symbol)
    while same_cal:
        operator = req_operator()
        function = operations[operator]
        num2 = float(input("What's the second number?: "))
        result = function(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        same_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if same_cal[0].lower() == 'y':
            same_cal = True
            num1 = result
        else:
            clear()
            calculator()

if __name__ == '__main__':
    calculator()