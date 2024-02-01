
from datetime import datetime


def string_to_date(date_object :str):
    """ Функция преобразует дату, записанную строкой, в правильный формат. """
    result = datetime.strptime(date_object, '%Y-%m-%d').date()
    return result