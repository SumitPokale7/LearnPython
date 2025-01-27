import os


Calculator = '''
_____________________
|  _________________  |
| | Masti        0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| 
'''


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(Calculator)
    should_Accumulate = True

    first_Number = float(input("What is the first number?: "))

    while should_Accumulate:
        for symbol in operations:
            print(symbol)
        operation_Calculate = str(input("Pick an operation: "))
        second_Number = float(input("What is the next number?: "))
        ans = operations[operation_Calculate](first_Number, second_Number)
        print(f"{first_Number} {operation_Calculate} {second_Number} = {ans}")
        
        continue_O = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")

        if continue_O == 'y':
            first_Number = ans
        else:
            should_Accumulate == False
            print("\n" * 20)
            calculator()


calculator()
