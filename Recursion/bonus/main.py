"""
Генерация всех корректных сбалансированных комбинаций круглых скобок
(параметр -- количество открывающих скобок).
Например:
in = "()"
out = ["(())", "()()"]
Внешне и внутренне несбалансированные комбинации считаются ошибочными:
"()))" ")(()" "(()" -- неверно

( = 1
) = -1
"""
def convert_res(data: list):
    """Return converted data from [-1; 1] to [(, )]"""
    res = []
    for i in data:
        string = ''
        for char in i:
            if char == 1:
                string += '('
            if char == -1:
                string += ')'
        res.append(string)
    return res

def brackets_comb(data: str):
    """Init and preparation"""
    brackets_count = len(data) * 2
    res = brackets_gen([], [], brackets_count)
    return convert_res(res)

def brackets_gen(data: list, res: list, brackets_count):
    """Return all legal combinations for input brackets"""
    if len(data) < brackets_count:
        if sum(data) > 0:
            t_data = data + [-1]
            brackets_gen(t_data, res, brackets_count)
        if sum(data) < brackets_count - len(data):
            t_data = data + [1]
            brackets_gen(t_data, res, brackets_count)
    else:
        res.append(data)
    return res
