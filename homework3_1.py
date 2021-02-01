# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
num1 = int(input('Enter first number: '))
num2 = int(input('Enter sekond number: '))

def num_div(*args):
    global num2
    try:
        num2 = int(num2)
    except ZeroDivisionError:
        print('Enter any number except 0')
        return num1 / num2
print(num_div(num1 / num2))
