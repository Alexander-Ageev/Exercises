"""Печать элементов списка с чётными индексами"""

def print_even_idx(data: list):
    """Init into_deep"""
    res = []
    return into_deep(data, res)

def into_deep (data: list, res: list):
    """Return data even indexes"""
    if data == []:
        return res
    res.append(data[0])
    return into_deep(data[2:], res)
