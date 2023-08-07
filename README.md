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

# Задача 3

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