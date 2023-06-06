from src.utils import load_operations, get_last_operations, format_date_string, format_number

# вывод сообщений о последних пяти успешных операций клиента
for i in get_last_operations(load_operations()):
    print(f'{format_date_string(i["date"])} {i["description"]}')

    if 'from' not in i.keys():
        print(f'{format_number(i["to"])}')
    else:
        print(f'{format_number(i["from"])} -> {format_number(i["to"])}')

    print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}')
    print()
