from src.utils import get_last_operations


def test_get_last_operations():
    """
    Тест количества операций, которые выводит функция get_last_operations
    """
    assert len(get_last_operations()) == 5
