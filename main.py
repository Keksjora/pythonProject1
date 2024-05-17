from src.widget import get_data, mask_account_card
from src.processing import filter_by_state, sort_by_date

print(mask_account_card("MasterCard 7158300734726758"))

print(mask_account_card("Счет 35383033474447895560"))

print(get_data("2018-07-11T02:26:18.671407"))

print(filter_by_state([{'id': "41428829", 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': "939719570", 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

print(sort_by_date([{'id': "41428829", 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': "939719570", 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': "594226727", 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': "615064591", 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
))