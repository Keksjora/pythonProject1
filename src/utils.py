import json


def get_transactions(file_path: str) -> list[dict]:
    """ Функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            repository = json.load(f)
            if isinstance(repository, list):
                return repository
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
