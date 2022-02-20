# Вычисление суммы цифр числа

def get_len(number: int):
    """Return length of number"""
    length = 1
    while number/10**length >= 1:
        length += 1
    return length

def get_digit(number: int, length: int):
    """Convert number to digits. Return sum of digit"""
    if length <= 1:
        return number
    else:
        base = 10**(length-1)
        remainder = number % base
        digit = number // base
        return digit + get_digit(remainder, length -1)

def dig_sum(number: int):
    """Return sum of digits"""
    number = abs(number)
    length = get_len(number)
    return get_digit(number, length)
