"""Проверка, является ли строка палиндромом"""

def check_palindrom(string: str):
    """Return True if string is palindrom"""
    if string == '':
        return True
    elif string[0] == string[-1]:
        return check_palindrom(string[1:-1])
    else:
        return False
