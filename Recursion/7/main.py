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

def sort_max_search(data: list):
    """Return second max value. Sort version"""
    if len(data) < 2:
        return None
    data.sort()
    return data[-2]
