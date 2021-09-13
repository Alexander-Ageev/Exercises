def counter (s):
    diff_char_counts = []
    for i in set(s):
        diff_char_counts.append(s.count(i))
    return diff_char_counts

# функция отделяет последовательности отличающихся символов от последовательности-исключения 
# Работает только если в исходных данных только одна последовательность-исключение
# возвращает массив [duplicate, exclusion]
def separator(l):
    result = []
    if len(l) == 2:
        result = l
        return result
    if l[0] == l[1]:
        result.append(l[0])
        result.append(l[-1])
    else:
        result.append(l[1])
        result.append(l[0])
    return result

def SherlockValidString(s):
    diff_symbols_count = sorted(counter(s)) # list of different char counts
    if len(set(diff_symbols_count)) <= 2:
        sequence_info = separator(diff_symbols_count)
        base_symbol_number, exclusion_symbol_number = sequence_info
        if len(set(diff_symbols_count)) == 1:# string [n, n, ... , n] type ('abc')
            input_string_valid = True
        elif min(counter(diff_symbols_count)) == 1 and exclusion_symbol_number - base_symbol_number == 1:# string [1, n, n, ... , n] type ('abbccdd')
            input_string_valid = True
        elif min(counter(diff_symbols_count)) == 1 and exclusion_symbol_number == 1:# string [n, n, ... , n, n+1] type ('abcdd')
            input_string_valid = True
        else:
            input_string_valid = False    
    else:
        input_string_valid = False
    return input_string_valid