def get_mask_card_number(card_number: str) -> str:
    """Функция принимает строку и возвращает маску карты"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(card_number: str) -> str:
    """Функция принимает строку и возвращает маску счёта"""
    masked_number = f"**{card_number[-4:]}"
    return masked_number
