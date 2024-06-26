import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    logger.info(f"Задаем формат маски для номера банковской карты {card_number}")

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(card_number: str) -> str:
    """Функция принимает строку и возвращает маску счёта"""
    logger.info(f"Проверяем правильность написания {card_number}")

    if len(str(card_number)) != 20:
        logger.error("Ошибка. Проверьте номер счета, он должен содержать 20 цифр")
        raise ValueError("Проверьте номер счета, он должен содержать 20 цифр")

    else:
        logger.info(f"Задаем формат маски для номера банковского счета {card_number}")
        masked_number = f"**{card_number[-4:]}"

    return masked_number
