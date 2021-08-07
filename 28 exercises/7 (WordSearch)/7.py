def slice_string(s, length):
    search_list = []
    if len(s) <= length and len(s) > 0:
        search_list.append(s)
        return search_list
    while len(s) > 0:
        portion = s[:length]
        index = s.rfind(' ', 0, length+1)
        if index == -1:
            s = s[length:].lstrip()
            search_list.append(portion)
        else:
            s = s[index+1:]
            search_list.append(portion[:index])
    return search_list

def check_portion(p, subs):
    for i in p:
        if i == subs:
            return 1
    return 0

def WordSearch(len, s, subs):
    result_list = []
    search_list = slice_string(s, len)
    for i in search_list:
        portion = i.split(' ')
        result_list.append(check_portion(portion, subs))
    return result_list     