def TankRush(H1, W1, S1, H2, W2, S2):
    map = S1.split(' ')
    for i in range(H1 - H2 + 1):
        for j in range(W1 - W2 + 1):
            chunk = ''
            for k in range(H2):
                chunk += " " + str(map[k+i][j:j+W2] )
            chunk = chunk.strip(' ')
            if chunk == S2:
                return True
    return False