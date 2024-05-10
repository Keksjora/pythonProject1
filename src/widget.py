from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция принимает строку и маскирует номер карты или счёта"""
    if len(number.split()[-1]) == 16:
        new_number = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{new_number}"
    elif len(number.split()[-1]) == 20:
        new_number = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{new_number}"
    return result


def get_data(str_data: str) -> str:
    """ "Функция принимает строку даты и форматирует её"""
    new_data = str_data[0:10].split("-")
    return ".".join(new_data[::-1])
