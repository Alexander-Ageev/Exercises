def search_number(s, e, field):
    template = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    N = len(field)
    M = len(field[0])
    n, m = 0, 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == s:
                n, m = i, j
                break
    for j in range(len(template)):
        y = n + template[j][0]
        x = m + template[j][1]
        if x in range(M) and y in range(N):
            if field[y][x] == e:
                return 1
    return 2**(0.5)

def round_length (length, digit):
    factor = 10 ** (digit + 1)
    length = int(length * factor)
    last_char = str(length)[-1]
    if int(last_char) > 4:
        length += 10
    length_str = str(length)[:-1]
    length = float(length_str)/(factor/10)
    return  length

def PatternUnlock(N, hits):
    field = [[6, 1, 9],
             [5, 2, 8],
             [4, 3, 7]]
    length = 0.0
    template = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    dec_separator = [',', '.']
    result = ''
    count = 0
    start_counter = 0
    for i in range(N-1):
        length += search_number(hits[i], hits[i+1], field)
    length = str(round_length(length, 5))
    for i in length:
        if i in template and count < 5:
            result += i
            count += 1 * start_counter
        elif i in dec_separator:
            start_counter = 1
    return result