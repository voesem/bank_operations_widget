import json
import os
from datetime import datetime
from operator import itemgetter


def load_operations():
    """
    Функция для чтения файла operations.json
    :return: возвращает данные файла operations.json
    """
    with open(os.path.join(os.path.dirname(__file__), 'operations.json'), encoding="utf-8") as f:
        operations_json = f.read()

        operations = json.loads(operations_json)

        return operations


def get_last_operations(operations):
    """
    Функция для вывода списка последних пяти успешных операций клиента
    :param operations: на вход функции подается список словарей с операциями
    :return: возвращает список последних пяти успешных операций клиента
    """
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


def format_number(number):
    """
    Функция для форматирования номера счета (в формате **XXXX)
    или карты клиента (в формате  XXXX XX** **** XXXX)
    :param number: строка, содержащая неформатированный номер счета или карты
    :return: возвращает номер счета (в формате **XXXX)
    или карты клиента (в формате  XXXX XX** **** XXXX)
    """
    number = number.split(' ')

    if len(number[-1]) == 20:
        return f'{" ".join(number[:-1])} {"*" * 2 + number[-1][-4:]}'
    elif len(number[-1]) == 16:
        n = 4
        hidden_number = number[-1][:6] + '*' * 6 + number[-1][-4:]
        number_split = [hidden_number[j:j + n] for j in range(0, len(hidden_number), n)]
        return f'{" ".join(number[:-1])} {" ".join(number_split)}'
