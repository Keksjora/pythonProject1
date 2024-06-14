# Сервисная часть виджета банковских операций

## Описание:

Проект сервисная часть виджета банковских операций - это веб-приложение на Python, который умеет отображать операции клиента

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```

## Использование:

1. В файле main.py можно в передавать различные именования номеров карт и счётов.
2. Функции можно передавать дату и время банковской операции и она будет возвращать корректную дату совершения выбранной операции.
3. Функции можно передать список всех банковских операция, она будет возвращать список необходмых операций.
4. Добавлены функции тестирующие проект.
5. Добавлены фикстуры для формирования входных данных для тестов.
6. Исползована параметризация в тестах для запуска одного теста с различным набором входных параметров.
7. Создал модуль generators.py для новых функций. 
8. В проекте реализован модуль decorators.py
9. Реализована функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
10. Реализована функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
11. Написаны тесты для новых функций с использованием Mock и path.


## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).
