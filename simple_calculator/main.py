import art

print(art.logo)

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    number1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:

        operation_invalid = True
        while operation_invalid:
            operation = input("Pick an operation: ")
            if operation in ['+','-','*','/']:
                operation_invalid = False
            else:
                print('You entered an invalid operation. Please try again!')

        number2 = float(input("What's the next number?: "))
       
        function = operations[operation]
        result = function(number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        
        cont_cal = input(f"Type 'y' to continue calculating with {result}, or others to start a new calculation: ")
        if cont_cal != 'y':
            should_continue = False
            calculator()
        else:
            number1 = result

calculator()