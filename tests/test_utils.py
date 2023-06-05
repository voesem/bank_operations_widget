from src.utils import get_last_operations, format_date_string


def test_get_last_operations():
    """
    Тест количества операций, которые выводит функция get_last_operations
    """
    assert len(get_last_operations()) == 5


def test_format_date_string():
    """
    Тест форматирования даты операции
    """
    assert format_date_string('2019-08-26T10:50:58.294041') == '26.08.2019'
    assert format_date_string('2019-07-03T18:35:29.512364') == '03.07.2019'
    assert format_date_string('2018-06-30T02:08:58.425572') == '30.06.2018'
