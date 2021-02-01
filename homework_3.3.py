# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов\

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

def my_func(num1, num2, num3):

    my_list = [num1, num2, num3]
    my_list.remove(min(num1, num2, num3))
    return sum(my_list)


print(my_func(num1, num2, num3))
