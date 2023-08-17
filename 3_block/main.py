try:
    with open('client.txt', 'r', encoding='utf-8') as f:
        file = f.read().split('\n')
except FileNotFoundError:
    print("Файл не найден")


def decorator(func):
    def wrapper(person, count):
        func(person)
        if count == 4:
            print("Вы получаете бесплатную плюшку!")

    return wrapper


@decorator
def greeting(person):
    print(f"Привет, {person}!")


i = 0
while not i > 4:
    if i < len(file):
        greeting(file[i], i)
        i += 1
    else:
        temp = input("Введите имя: ")
        greeting(temp, i)
        i += 1
