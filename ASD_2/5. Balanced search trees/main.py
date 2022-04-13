"""Модуль описывает функцию балансировки дерева поиска"""

def GetMiddleIndex(array: list):
    "Возвращает индекс середины массива. Если массив пустой - возвращает -1"
    size = len(array)
    if size == 0:
        mid_index = -1
    else:
        mid_index = size // 2
    return mid_index

def GenArray(roots: list, parts: list):
    """
    Получает на вход отсортированный по возрастанию массив.
    Возвращает массив, описывающий структуру сбалансированного дерева
    """
    new_parts = []
    for i in parts:
        mid = GetMiddleIndex(i)
        if mid != -1:
            left_branch = i[0: mid]
            right_branch = i[mid+1:]
            roots.append(i[mid])
            new_parts += [left_branch, right_branch]
    if new_parts != []:
        GenArray(roots, new_parts)
    return roots

def GenerateBBSTArray(a: list):
    """Инициализация GenArray"""
    a.sort()
    array = GenArray([], [a])
    return array
