def concat_strings(*args: str) -> str | None:
    try:
        result_string = ''
        if len(args) < 2:
            raise ValueError("Необходимо минимум 2 аргумента")
        for arg in args:
            if isinstance(arg, str):
                result_string += f'{arg.strip()} '
            else:
                raise TypeError("Все аргументы должны быть строками")

        result_string = result_string.strip()
        if not len(result_string):
            raise ValueError("Передавать пустые строки тоже не стоит")
        return result_string

    except TypeError as e:
        print(f"Произошла ошибка: {e}")
        return None
    except ValueError as e:
        print(f"Произошла ошибка: {e}")
        return None


if __name__ == "__main__":
    result = concat_strings("Hello", "world!")
    print('Function result:', result)
