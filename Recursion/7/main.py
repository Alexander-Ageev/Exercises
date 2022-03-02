"""
Нахождение второго максимального числа в списке
(с учётом, что максимальных может быть несколько, если они равны)
"""

def linear_max_search(data: list):
    """Return second max value. Loop version"""
    if len(data) < 2:
        return None
    big = max(data[0:2]) # max value
    low = min(data[0:2]) # second max value; max >= low
    for i in data[2:]:
        if i > big:
            low = big
            big = i
        elif big >= i > low:
            low = i
    return low

def max_search(data: list):
    """Return second max value. Clear version"""
    big = None
    low = None
    for i in data:
        if big is None or i > big:
            low = big
            big = i
        elif low is None or big >= i > low:
            low = i
    return low

def rec_max_search(data: list):
    """Init"""
    big_low = [None, None]
    return loop_it(data, big_low)[1]

def loop_it(data:list, big_low: list):
    """Return second max value. Recursion version"""
    if data == []:
        return big_low
    if big_low[0] is None or big_low[0] < data[0]:
        big_low = [data[0], big_low[0]]
    elif big_low[1] is None or big_low[1] < data[0] <= big_low[0]:
        big_low[1] = data[0]
    return loop_it(data[1:], big_low)
