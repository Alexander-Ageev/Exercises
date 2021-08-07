def octacode(number):
    result = 0
    octo = str(number)[::-1]
    for i in range(len(octo)):
        result += int(octo[i]) * 8**i
    return result
# по условию наличие символов A-F во входном массиве не предусмотрено
def hexacode(number):
    result = 0
    hexo = str(number)[::-1]
    for i in range(len(hexo)):
        result += int(hexo[i]) * 16**i
    return result   

def UFO(N, data, octal):
    result = []
    for i in range(N):
        if octal:
            result.append(octacode(data[i]))
        else:
            result.append(hexacode(data[i]))
    return result