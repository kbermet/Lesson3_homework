# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('Enter yourr name: ')
surname = input('Enter your surname: ')
birth = input('Enter your birth date: ')
city = input('Enter your city: ')
email = input('Enter your email: ')
tel = input('Enter your telephone: ')


def prof(**kwargs):
    return prof()


print(f"You are {name} {surname}, born on {birth} in {city}, your email is {email} and tel:{tel}")
