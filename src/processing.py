def filter_by_state(list_dict: list, state="EXECUTED"):
    """"Функция,которая принимает на вход список словарей и значение для ключа
state и возвращает новый список """
    filtred_list = []
    for list in list_dict:
        if list.get("state") == state:
            filtred_list.append(list)
    return filtred_list

def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """"Функция,которая принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы по убыванию даты """
    return sorted(list_dict, key=lambda x: x["date"], reverse=direction)

