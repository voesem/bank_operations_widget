from operator import itemgetter

import json


def get_last_operations():
    """
    Функция для чтения файла operations.json и вывода
    списка последних пяти успешных операций клиента
    :return: возвращает список последних пяти успешных операций клиента
    """
    with open('C:/Users/Владимир/PycharmProjects/bank_operations_widget/operations.json', encoding="utf-8") as f:
        operations_json = f.read()

        operations = json.loads(operations_json)

        operations = [
            operation for operation in operations if 'date' in operation.keys() and operation['state'] == 'EXECUTED'
        ]

        operations_sorted = sorted(operations, key=itemgetter('date'), reverse=True)

        return operations_sorted[:5]
