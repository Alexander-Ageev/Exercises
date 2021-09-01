def matrix_size(s):
    n = len(s) ** 0.5
    row = int(n)
    column = int(n + 0.5)
    size = []
    if row * column < len(s):
        size.extend([row+1, column])
    else:
        size.extend([row, column])
    return size

def encode_string(s):
    s = ''.join(s.split(' '))
    size = matrix_size(s)
    row = size[0]
    column = size[1]
    encode = ''
    for i in range(column):
        for j in range(row):
            if i + j * column < len(s):
                encode += s[i + j * column]
        encode += ' '
    encode = encode.strip(' ')
    return encode

def decode_string(s):
    word_array = s.split(' ')
    row = len(word_array)
    column = len(word_array[0])
    decode = ''
    for i in range(column):
        for j in range(row):
            try:
                decode += word_array[j][i]
            except:
                pass
    decode = decode.strip(' ')
    return decode

def TheRabbitsFoot(source_string, encode_mode): # encode = true: зашифровать; encode = false: расшировать
    if encode_mode:
        encode = encode_string(source_string)
        return encode
    else:
        decode = decode_string(source_string)
        return decode
