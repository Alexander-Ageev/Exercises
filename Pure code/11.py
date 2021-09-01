# Вынес блоки кода в отдельные  функции subtraction, calc_foundation_count, result_verification
# Переименовал большое количество переменных, убрал переназначение переменных - это позволило более осмысленно отразить изменения данных
FOUNDATION = 4 #Количество цифр, на которое разбивается число
MAX_FOUNDATION_NUMBER = int('9'*FOUNDATION)

def pad_string(input_string, length):
    pad_count = length - len(input_string)
    result_string = "0" * pad_count + input_string
    return result_string

def calc_foundation_count(s1, s2):
    count = max(len(s1), len(s2))//FOUNDATION
    need_more_digit = max(len(s1), len(s2)) % FOUNDATION != 0
    if need_more_digit:
        count += 1
    return count 

def result_verification(input_list, length_string):
    input_string = input_list[0]
    negative = input_list[1]
    result_string = input_string.lstrip('0')
    if result_string == '':
        result_string = '0'
    if negative:
        s1 = result_string
        s2 = '1' + '0' * length_string
        result_string = BigMinus(s2, s1)
    return result_string  

def portion_subtraction(n1, n2, discharge_transfer):
    sub_result = n1 + discharge_transfer - n2
    if sub_result < 0:
        sub_result = MAX_FOUNDATION_NUMBER - n2 + discharge_transfer + 1 + n1
        discharge_transfer = -1
    else:
        discharge_transfer = 0
    result = pad_string(str(sub_result), FOUNDATION)
    return [result, discharge_transfer]

def subtraction(s1, s2, foundation_count):
    subtraction_result = ''
    discharge_transfer = 0
    for i in range(foundation_count):
        start_index = FOUNDATION * (foundation_count - (i+1))
        stop_index = FOUNDATION * (foundation_count-i)
        s1_portion = int(s1[start_index : stop_index])
        s2_portion = int(s2[start_index : stop_index])
        temp = portion_subtraction(s1_portion, s2_portion, discharge_transfer)
        portion_result = temp[0]
        discharge_transfer = temp[1]
        subtraction_result = portion_result + subtraction_result
        number_is_negative = discharge_transfer < 0
    return [subtraction_result, number_is_negative]

def BigMinus(input_s1, input_s2):
    foundation_count = calc_foundation_count(input_s1, input_s2)
    max_length = foundation_count * FOUNDATION
    padded_s1 = pad_string(input_s1, max_length)
    padded_s2 = pad_string(input_s2, max_length) 
    subtraction_result = subtraction(padded_s1, padded_s2, foundation_count)   
    result = result_verification(subtraction_result, max_length)   
    return result

# В остальных заданиях все блоки кода разнесены по смыслу и не образуют фрагментов с большими окнами уязвимости
# Поля в классах так же инициализируются все и сразу