import json
import os.path
import re
from collections import Counter

import pandas as pd

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


def get_transactions(json_file_path: str) -> list[dict]:
    """Функцию, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращает пустой список."""
    try:
        logger.info(f"Открытие файла {json_file_path}")
        with open(json_file_path, "r", encoding="utf-8") as f:
            repository = json.load(f)
            logger.info(f"Проверяем, что файл {json_file_path} не пустой")
            if isinstance(repository, list):
                return repository
            else:
                logger.info(f"Возращаем пустой словарь, если файл {json_file_path} пустой")
                return []

    except Exception:
        logger.error("Ошибка")
        return []


def read_transactions_from_csv(csv_file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(csv_file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []  # Возвращаем пустой список в случае ошибки


def read_transactions_from_excel(excel_file_path: str) -> list:
    """Считывает финансовые операции из XLSX-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(excel_file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении XLSX-файла: {e}")
        return []  # Возвращаем пустой список в случае ошибки


def filter_transactions_by_description(transactions: list, search_string: str) -> list:
    """
    Фильтрует список транзакций по описанию.
    """
    filtered_transactions = []
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        if re.search(search_string.lower(), description):
            filtered_transactions.append(transaction)
    return filtered_transactions


def count_transactions_by_category(transactions: list, categories: list) -> dict:
    """
    Подсчитывает количество транзакций по категориям с использованием Counter.
    """
    category_counts = Counter()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if re.search(category.lower(), description):
                category_counts[category] += 1
    return category_counts
