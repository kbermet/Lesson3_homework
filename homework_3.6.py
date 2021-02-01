# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
# из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
# буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func():
    for word in input("Type a word in latin with a space:\n").split():
        letters = 0
        for letter in word:
            if 97 <= ord(letter) <= 122:
                letters += 1
        print(word.title() if letters == len(word) else f"{word} - type words only in lowercase.")

int_func()