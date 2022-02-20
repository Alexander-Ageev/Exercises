# Возведение числа N в степень M

def power(n, m):
    if m < 0 :
        return 1 / (n * power(n, abs(m)-1))
    elif m > 0:
        return n * power(n, m-1)
    else:
        return 1