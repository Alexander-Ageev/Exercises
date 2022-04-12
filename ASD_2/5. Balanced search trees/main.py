"""Модуль описывает метод создания сбалансированного дерева поиска"""

def GetMiddleIndex(array: list):
    size = len(array)
    if size == 0:
        mid_index = -1
    else:
        mid_index = size // 2
    return mid_index

def GenArray(array: list, left: list, right: list):
    left_child_index = GetMiddleIndex(left)
    if left_child_index != -1:
        array.append(left[left_child_index])
        GenArray(array, left[0: left_child_index], left[left_child_index+1:])
    
    right_child_index = GetMiddleIndex(right)
    if right_child_index != -1:
        array.append(right[right_child_index])
        GenArray(array, right[0: right_child_index], right[right_child_index+1:])
    return array

"""
def GenArray(array: list, left: list, right: list):
    left_child_index = GetMiddleIndex(left)
    if left_child_index == -1:
        return array
    right_child_index = GetMiddleIndex(right)
    if right_child_index == -1:
        return array
    array.append(left[left_child_index])
    array.append(right[right_child_index])
    GenArray(array, left[0: left_child_index], left[left_child_index+1:])
    GenArray(array, right[0: right_child_index], right[right_child_index+1:])
    return array
"""

def GenerateBBSTArray(a: list):
    a.sort()
    root_index = GetMiddleIndex(a)
    root = a[root_index]
    left = a[0: root_index]
    right = a[root_index+1:]
    array = GenArray([root], left, right)
    return array