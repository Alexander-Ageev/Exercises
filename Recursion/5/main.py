"""Печать только чётных значений из списка"""

def print_even_value(data: list):
    """Init list_parsing function"""
    res = []
    return list_parsing(data, res)

def list_parsing(data: list, res: list):
    """Return only even values from data"""
    if data == []:
        return res
    elif data[0] % 2 == 0:
        res.append(data[0])
    return list_parsing(data[1:], res)
