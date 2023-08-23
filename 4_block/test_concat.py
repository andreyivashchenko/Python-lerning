from main import concat_strings


def test_concat():
    assert concat_strings('Hello', 'world!') == "Hello world!"
    assert concat_strings('Я', 'сегодня    ', '      ходил', 'в', 'магазин') == "Я сегодня ходил в магазин"
    assert concat_strings('', '') is None
    assert concat_strings(32, True) is None
    assert concat_strings('hello') is None
    assert concat_strings() is None


