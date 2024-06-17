import json
import os.path

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
