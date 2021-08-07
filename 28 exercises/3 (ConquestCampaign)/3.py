def check_free_square (battlefield):
    for i in range(len(battlefield)):
        for j in range(len(battlefield[i])):
            if battlefield[i][j] == '0':
                return True
    return False

def descent(locations, battlefield):
    for i in range(len(locations)//2):
        battlefield[locations[i*2]][locations[i*2+1]] = '+'
    return locations

def calc_descent_locations(n, m, battlefield):
    descent_template = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    locations = []
    N = len(battlefield)
    M = len(battlefield[0])
    for j in range(len(descent_template)):
        y = n + descent_template[j][0]
        x = m + descent_template[j][1]
        if x in range(M) and y in range(N):
            if battlefield[y][x] == '0':
                locations.extend([y, x])
    return locations

def conquest(locations, battlefield):
    descent_locations = []
    for i in range(len(locations)//2):
        battlefield[locations[i*2]][locations[i*2+1]] = '*'
        descent_locations.extend(calc_descent_locations(locations[i*2], locations[i*2+1], battlefield))
    return descent_locations

def ConquestCampaign(N, M, L, battalion):
    battlefield = [['0'] * M for k in range(N)]
    day = 1
    descent_locations = [i - 1 for i in battalion]
    conquest_locations = descent(descent_locations, battlefield)
    while check_free_square(battlefield):
        descent_locations = conquest(conquest_locations, battlefield)
        conquest_locations = descent(descent_locations, battlefield)
        day += 1
    return day