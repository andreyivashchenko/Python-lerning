def decorator(func):
    counter = 0

    def wrapper(person):
        nonlocal counter
        counter += 1
        func(person)
        if counter == 5:
            print("Вы получаете бесплатную плюшку!")
            counter = 0
    return wrapper


@decorator
def greeting(person):
    print(f"Привет, {person}!")


try:
    with open('client.txt', 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            greeting(line.strip())
except FileNotFoundError:
    print("Файл не найден")


while True:
    user_input = input("Введите имя посетителя (или exit для выхода): ")
    if user_input.lower() == "exit":
        print("Программа завершена.")
        break
    else:
        greeting(user_input)
