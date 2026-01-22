# utils/helpers.py

def assert_is_positive_int(value):
    """Проверяет, что значение — положительное целое число"""
    assert isinstance(value, int), f"Ожидался int, получено {type(value).__name__}"
    assert value > 0, f"Значение должно быть > 0, получено {value}"
