"""
Нахождение второго максимального числа в списке
(с учётом, что максимальных может быть несколько, если они равны)
    Return value format: (max_value, error_code)
    error_code = 0: no error
    error_code = -1: incorrect data
"""

def linear_max_search(data: list):
    """Return second max value. Loop version"""
    if len(data) < 2:
        return (0, -1)
    big = max(data[0:2]) # max value
    low = min(data[0:2]) # second max value; max >= low
    for i in data[2:]:
        if i > big:
            low = big
            big = i
        elif big >= i > low:
            low = i
    return (low, -1)

def max_search(data: list):
    """Return second max value. Clear version"""
    if len(data) < 2:
        return (0, -1)
    if data[0] > data[1]:
        big = data[0]
        low = data[1]
    else:
        big = data[1]
        low = data[0]
    for i in data:
        if i > big:
            low = big
            big = i
        elif big >= i and i > low:
            low = i
    return (low, 0)

def rec_max_search(data: list):
    """Init"""
    if len(data) < 2:
        return (0, -1)
    if data[0] > data[1]:
        big_low = [data[0], data[1]]
    else:
        big_low = [data[1], data[0]]
    return (loop_it(data, big_low)[1], 0)

def loop_it(data:list, big_low: list):
    """Return second max value. Recursion version"""
    if data == []:
        return big_low
    if big_low[0] < data[0]:
        big_low = [data[0], big_low[0]]
    elif big_low[1] < data[0] and data[0] <= big_low[0]:
        big_low[1] = data[0]
    return loop_it(data[1:], big_low)
