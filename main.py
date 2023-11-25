import math


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на 0"


def exponentiation(a, b):
    return a ** b


def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Ошибка: отрицательное число"


def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Ошибка: отрицательное число"


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def tangent(a):
    return math.tan(a)


def validate_number_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Ошибка: введите числовое значение")


def validate_operation_input(prompt, valid_operations):
    while True:
        operation = input(prompt)
        if operation in valid_operations:
            return operation
        else:
            print("Ошибка: введите допустимую операцию")


def run_calculator():
    print("Доступные операции: +, -, *, /, **, sqrt, !, sin, cos, tan")
    valid_operations = ['+', '-', '*', '/', '**', 'sqrt', '!', 'sin', 'cos', 'tan']
    operation = validate_operation_input("Выберите операцию: ", valid_operations)

    if operation in ['+', '-', '*', '/', '**']:
        num1 = validate_number_input("Введите первое число: ")
        num2 = validate_number_input("Введите второе число: ")

        if operation == '+':
            result = addition(num1, num2)
        elif operation == '-':
            result = subtraction(num1, num2)
        elif operation == '*':
            result = multiplication(num1, num2)
        elif operation == '/':
            result = division(num1, num2)
        elif operation == '**':
            result = exponentiation(num1, num2)

    elif operation in ['sqrt', '!']:
        num1 = validate_number_input("Введите число: ")

        if operation == 'sqrt':
            result = square_root(num1)
        elif operation == '!':
            result = factorial(num1)

    elif operation in ['sin', 'cos', 'tan']:
        num1 = validate_number_input("Введите число: ")

        if operation == 'sin':
            result = sine(num1)
        elif operation == 'cos':
            result = cosine(num1)
        elif operation == 'tan':
            result = tangent(num1)

    print("Результат:", result)


run_calculator()