def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """ "Функция фильтрует список словарей по ключу state"""
    filtred_list = []
    for ld in list_dict:
        if ld.get("state") == state:
            filtred_list.append(ld)
    return filtred_list


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """ "Функция сортирует словари по убыванию даты"""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=direction)
    return sorted_list
