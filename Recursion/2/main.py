# Вычисление суммы цифр числа

def dig_sum(number):
    """Return sum of digits"""
    if number < 0:
        number = abs(number)
    if number > 9:
        dig = number % 10
        rem = number // 10
        return dig + dig_sum(rem)
    else:
        return number
