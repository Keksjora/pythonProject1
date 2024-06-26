import os

# from src.decorators import log
from src.external_api import convert_to_rub
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.utils import (
    count_transactions_by_category,
    filter_transactions_by_description,
    get_transactions,
    read_transactions_from_csv,
    read_transactions_from_excel,
)
from src.widget import get_data, mask_account_card

print(mask_account_card("MasterCard 7158300734726758"))

print(mask_account_card("Счет 35383033474447895560"))

print(get_data("2018-07-11T02:26:18.671407"))

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions)["id"])
# для разделения результата
print()

descriptions = transaction_descriptions(transactions)
for i in range(5):
    print(next(descriptions))
# для разделения результата
print()

for card_number in card_number_generator(1, 5):
    print(card_number)

# @log(filename="mylog.txt")
# def my_function(x, y):
#     """ "Функция вызова декоратора с файлом сохранения mylog.txt"""
#     return x + y
#
#
# my_function(1, 2)
#
#
# @log()
# def my_function_1(x, y):
#     """ "Функция вызова декоратора без файла сохранения и вывод в консоль"""
#     return x + y
#
#
# my_function_1(1, 2)
#
#
# @log()
# def my_function_error(x, y):
#     """ "Функция вызова декоратора с ошибкой и сохранения вывода в файл mylog.txt"""
#     return x / y
#
#
# my_function_error(1, 0)

json_file_path = os.path.join("data", "operations.json")
new_transactions = get_transactions(json_file_path)
print(new_transactions)

for transaction in new_transactions:
    rub_amount = convert_to_rub(transaction)
    print(f"Transaction amount in Rub: {rub_amount}")

csv_file_path = "C:/Users/Admin/PycharmProjects/pythonProject1/data/transactions_csv.csv"
new_transactions_csv = read_transactions_from_csv(csv_file_path)
print(new_transactions_csv)

excel_file_path = "C:/Users/Admin/PycharmProjects/pythonProject1/data/transactions_excel.xlsx"
new_transactions_excel = read_transactions_from_excel(excel_file_path)
print(new_transactions_excel)


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_type = input(
        """''
        Выберите необходимый пункт меню:\n1.
        Получить информацию о транзакциях из JSON-файла\n2.
        Получить информацию о транзакциях из CSV-файла\n3.
        Получить информацию о транзакциях из XLSX-файла\n
        """
        ""
    )
    if file_type not in ["1", "2", "3"]:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    if file_type == "1":
        transactions_n = new_transactions
    elif file_type == "2":
        transactions_n = new_transactions_csv
    else:
        transactions_n = new_transactions_excel

    if not transactions_n:
        print("Не удалось загрузить данные о транзакциях.")
        return

    status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    ).lower()
    if status not in ["executed", "canceled", "pending"]:
        print("Неверный статус. Пожалуйста, выберите EXECUTED, CANCELED или PENDING.")
        return

    def filter_transactions_by_status(transactions_list, status):
        return [t for t in transactions_list if t.get("state", "").lower() == status]

    filtered_transactions = filter_transactions_by_status(transactions, status)

    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower() == "да"
    if sort_by_date:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if sort_order == "по возрастанию":
            filtered_transactions = sorted(filtered_transactions, key=lambda t: t["date"])
        elif sort_order == "по убыванию":
            filtered_transactions = sorted(filtered_transactions, key=lambda t: t["date"], reverse=True)

    rub_only = input("Выводить только рублевые тразакции? Да/Нет").lower() == "да"
    if rub_only:
        filtered_transactions = [
            t
            for t in filtered_transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code", "") == "RUB"
        ]

    search_description = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower() == "да"
    )
    if search_description:
        search_string = input("Введите строку для поиска:\n")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под Ваши условия фильтрации.")
        return

    categories = ["перевод", "покупка", "оплата", "выдача", "возврат"]
    category_counts = count_transactions_by_category(filtered_transactions, categories)

    print("Результаты фильтрации:\n")
    for transaction_n in filtered_transactions:
        date = transaction_n.get("date", "")
        description = transaction_n.get("description", "")
        account = transaction_n.get("from", "")
        amount = transaction_n.get("operationAmount", {}).get("amount", "")
        currency = transaction_n.get("operationAmount", {}).get("currency", {}).get("code", "")
        print(f"{date} {description}nСчет {account}nСумма: {amount} {currency}")

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")
    print("Количество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
