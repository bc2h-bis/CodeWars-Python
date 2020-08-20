# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.

# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"

def calculator(x, y, op):
    # control x, y are number and op is a sign operator
    # then realize calculation
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) and op == '+':
        return x + y
    elif isinstance(x, (int, float)) and isinstance(y, (int, float)) and op == '-':
        return x - y
    elif isinstance(x, (int, float)) and isinstance(y, (int, float)) and op == '/':
        return x / y
    elif isinstance(x, (int, float)) and isinstance(y, (int, float)) and op == '*':
        return x * y
    elif isinstance(x, (int, float)) and isinstance(y, (int, float)) and op == '%':
        return x % y
    # else return "unknown value" message
    else:
        return "unknown value"


# tests
print(calculator(6, 2, '+'))
print(calculator(6, 2, '+') == 8)
print(calculator(4, 3, '-') == 1)
print(calculator(5, 5, '*') == 25)
print(calculator(5, 4, '/') == 1.25)
print(calculator(6, 2, '&') == "unknown value")
print(calculator(6, 'p', '+') == "unknown value")

# Other soluces

# def calculator(x, y, op):
# return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'

# def calculator(x, y, op):
# try:
#     return {'+': x + y, '-': x - y, '*': x * y, '/': x / y}[op]
# except (TypeError, KeyError):
#     return 'unknown value'
