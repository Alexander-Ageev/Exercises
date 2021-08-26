def slice_string(input_string, slicing_width):
    search_list = []
    if 0 < len(input_string) <= slicing_width:
        search_list.append(input_string)
        return search_list
    while len(input_string) > 0:
        portion = input_string[:slicing_width]
        index = input_string.rfind(' ', 0, slicing_width+1)
        if index == -1:
            input_string = input_string[slicing_width:].lstrip()
            search_list.append(portion)
        else:
            input_string = input_string[index+1:]
            search_list.append(portion[:index])
    return search_list

def check_portion(string, find_string):
    for i in string:
        if i == find_string:
            return 1
    return 0

def WordSearch(max_width, input_string, find_string):
    result_list = []
    search_list = slice_string(input_string, max_width)
    for i in search_list:
        portion = i.split(' ')
        result_list.append(check_portion(portion, find_string))
    return result_list     