"""
Расчёт длины списка,
для которого разрешена только одна операция удаления первого элемента pop(0)
"""

def get_len(data:list):
    '''Return length of list'''
    if data != []:
        data.pop(0)
        return 1 + get_len(data)
    else:
        return 0
