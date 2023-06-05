from operator import itemgetter
from datetime import datetime

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


def format_date_string(string):
    """
    Функция для приведения даты совершения операции к формату ДД.ММ.ГГГГ
    :param string: строка, содержащая неформатированные дату и время совершения операции
    :return: возвращает дату в формате ДД.ММ.ГГГГ
    """
    date_obj = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%f')
    date_string = date_obj.strftime('%d.%m.%Y')

    return date_string
