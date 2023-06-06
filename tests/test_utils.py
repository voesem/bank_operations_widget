from src.utils import load_operations, get_last_operations, format_date_string, format_number


def test_get_last_operations():
    """
    Тест количества операций, которые выводит функция get_last_operations
    """
    assert len(get_last_operations(load_operations())) == 5


def test_format_date_string():
    """
    Тест форматирования даты операции
    """
    assert format_date_string('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert format_date_string('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert format_date_string('2018-06-30T02:08:58.425572') == '30.06.2018'


def test_format_number():
    """
    Тест форматирования номера счета или карты
    """
    assert format_number('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'
    assert format_number('Visa Platinum 8990922113665229') == 'Visa Platinum 8990 92** **** 5229'
    assert format_number('Счет 48894435694657014368') == 'Счет **4368'
