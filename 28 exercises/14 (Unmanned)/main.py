def Unmanned(L, N, track):
    current_time = 0
    for i in range(len(track)):
        if track[i][0] < L:
            if i == 0:
                current_time = track[0][0] 
            else:
                current_time += track[i][0] - track[i-1][0]
            cycle = track[i][1] + track[i][2]
            if current_time % cycle < track[i][1]:
                waiting_time = track[i][1] - current_time % cycle 
                current_time += waiting_time
            last_light_index = i
        else:
            break
    if current_time:
        current_time += L - track[last_light_index][0]
    else:
        current_time = L
    
    return current_time