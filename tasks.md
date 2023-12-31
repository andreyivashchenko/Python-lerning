# Задача 1 (*Выполнено*)
*Основные темы:*
- Основы фреймверка pytest
- Тестовые методы
- Asserts

## Задание
1) Создать функцию проводящую конкатенацию для двух строк.
2) Создать на pytest тестовые сценарии проверяющую работу этой функции


# Задача 2 (*Выполнено*)
*Основные темы:*
- Классы 
- Константы, защищенные, статичные, приватные методы 
- Абстрактный класс и модуль АВС 
- Тест-классы в Pytest

## Задание
1) Создать класс для сущности ApiRequest с атрибутами:
   - "тип запроса", 
   - "payload".
   
    Описать методы смены payload.

2) Создать тест-класс для pytest для тестирования методов класса ApiRequest: 
   - Проверка типа созданного ApiRequest
   - Проверка payload
   - Смена payload

# Задача 3 (*Выполнено*)

*Основные темы:*
- Pytest: Маркеры, Фикстуры, скоуп
- Работа с json 
- Библиотека Pydentic 
- Библиотека request

## Задание 
Используя изученные библиотеки и инструменты написать класс тестов для sample API 
https://petstore.swagger.io/ для раздела методов /pet:
- POST /Pet 
- PUT /pet 
- GET /pet/findByStatus 
- GET /pet/{petId} 
- POST /pet/{petId} 
- DELETE /pet/{petId}

Отмаркировать тесты на создание и редактирования для раздельного запуска.

# Задача 4 

*Основные темы:*
- Виртуальное окружение
- Python и работа с базами данных
- Allure-репорты

## Задание
Для работы понадобится перейти на https://uibakery.io/sql-playground и использовать **postgres data base "Booking website database"** 

Используя указанную базу данных, для таблицы *users* написать автоматические тестовые сценарии:
- создания пользователя 
- получения информации о пользователе 
- обновления информации 
- удаления пользователя

Для выполненных тестов должен формироваться отчет в формате **allure**.

# Задача 5 

*Основные темы:*
- Selenium
- Page Object
- Локаторы и их виды
- Методы работы с веб интерфейсом

## Задание 

Используя https://www.saucedemo.com/ реализовать следующие сценарии с использованием Selenium + pytest:
- Логин/Логаут
- Проверить логин под заблокированным пользователем (locked_out_user)
- Для каждого товара в магазине провести тест на возможность покупки (6 параметризованных сценариев)
- Проверить, что при добавлении/удалении товара в корзину у корзины изменяется счетчик
- Проверить работу сортировок (4 вида)
