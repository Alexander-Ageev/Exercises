def BiggerGreater(input):
    result = ''
    input_list = [i for i in input ]
    len_part = 2 # length current partition
    length = len(input_list)
    last_char = input_list[length - 1]
   
    while len_part <= length:
        current_char = input_list[ length - len_part ]
        part = input_list[length - len_part:length]
        sorted_part = sorted(part, reverse=True)
        if part != sorted_part:
            if last_char > current_char:
                replaced_char = part.pop(len_part - 1)
                sorted_part = part
                result = ''.join( input_list[0: length - len_part] ) + replaced_char + ''.join(sorted(part))
                break
            else:
                tmp = sorted(list (set (part)))
                replaced_char = tmp[tmp.index(part[0])+1]
                tmp = part.pop(part.index(replaced_char))
                sorted_part = part
                result = ''.join( input_list[0: length - len_part] ) + replaced_char + ''.join(sorted(part))
                break                
        else:
            len_part += 1
    return result