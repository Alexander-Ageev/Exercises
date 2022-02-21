"""
Расчёт длины списка,
для которого разрешена только одна операция удаления первого элемента pop(0)
"""

def get_len(data:list):
    '''Return length of list'''
    try:
        data.pop(0)
        return 1 + get_len(data)
    except ValueError:
        return 0
