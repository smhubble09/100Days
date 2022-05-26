from calculator_art import logo

#Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Dictionary
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    continue_operation = True
    while continue_operation:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ")
        if should_continue == "y":
            num1 = answer
        else:
            continue_operation = False
            calculator()

calculator()