# Возведение числа N в степень M

def power(number, degree):
    """ return number in degree with recursion"""
    if degree < 0 :
        return 1 / (number * power(number, abs(degree)-1))
    elif degree > 0:
        return number * power(number, degree-1)
    else:
        return 1
