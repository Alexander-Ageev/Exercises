BASE = 4 #Количество цифр, на которое разбивается число
BASE_Number = int('9'*BASE)

def base_sub(n1, n2, mode):
    result = ['', 0]
    result[0] = n1 + mode - n2
    if result[0] < 0:
        result[0] = BASE_Number - n2 + mode + 1 + n1
        result[1] = -1
    result[0] = fill_string(str(result[0]), BASE)
    return result

# Функция дополняет слева нулями до длины len строку с числом
def fill_string(s, length):
    fill_count = length - len(s)
    s = "0" * fill_count + s
    return s

def BigMinus(s1, s2):
    result = ''
    temp = [0, 0]
    need_more_digit = max(len(s1), len(s2)) % BASE != 0
    if need_more_digit:
        base_count = ( max(len(s1), len(s2))//BASE ) + 1
    else:
        base_count =   max(len(s1), len(s2))//BASE
    max_length = base_count * BASE
    s1 = fill_string(s1, max_length)
    s2 = fill_string(s2, max_length)
    for i in range(base_count):
        s1_portion = int( s1[ BASE * (base_count - (i+1)) : BASE * (base_count-i)] )
        s2_portion = int( s2[ BASE * (base_count - (i+1)) : BASE * (base_count-i)] )
        temp = base_sub(s1_portion, s2_portion, temp[1])
        result = temp[0] + result
    result = result.lstrip('0')
    if result == '':
        result = '0'
    # Если результат последнего вычитания отрицательный
    if temp[1] == -1:
        s1 = result
        s2 = '1' + '0' * max_length
        result = BigMinus(s2, s1)
    return result