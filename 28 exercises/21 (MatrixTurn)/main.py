def get_ring(data, r):
    M = len(data)
    N = len(data[0])
    ring = []
    left_column = ''
    right_column = ''
    upper_line = data[r][r:N- r]
    lower_line = data[M -1 - r][r : N - r]
    for i in range(len(data) - 1 - r):
        if i > r:
            left_column += data[i][r]
            right_column += data[i][N - 1 - r]
    ring.extend([upper_line, right_column, lower_line[::-1], left_column[::-1]])
    return ring
    
def turn_ring(ring, turn):
    ring_str = ''.join(ring)
    ring_str = ring_str[-turn:] + ring_str[0: -turn]
    result = []
    for i in ring:
        result.append(ring_str[0: len(i)])
        ring_str = ring_str[len(i):]
    return result

def set_ring(ring, r, data):
    M = len(data)
    N = len(data[0])
    upper_line = ring[0]
    right_column = ring[1]
    lower_line = ring[2]
    lower_line = lower_line[::-1]
    left_column = ring[3]
    left_column = left_column[::-1]
    for i in range(len(data)):
        if  i == r:
            data[i] = data[i][0: r] + upper_line + data[i][N - r: ]
        elif i == M - 1 - r:
            data[i] = data[i][0: r] + lower_line + data[i][N - r : ]
        elif r < i < M - 1 - r:
            bl = data[i][0: r]
            l = left_column[i - 1 - r]
            m = data[i][r + 1: N - 1 - r]
            rr = right_column[i - 1 - r]
            ar = data[i][N - r + 1: ]
            data[i] = bl + l + m + rr + ar
        else:
            pass
    return data


def MatrixTurn(data, M, N, T):
    for current_radius in range(min(M,N)//2):
        ring = get_ring(data, current_radius)
        ring = turn_ring(ring, T)
        data = set_ring(ring, current_radius, data)
    return data
    



