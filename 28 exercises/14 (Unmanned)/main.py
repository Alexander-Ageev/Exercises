CURRENT_TIME = 0
RED_LIGTH_TIME = 1
GREEN_LIGHT_TIME = 2

def Unmanned(L, N, track):
    current_time = 0
    for i in range(len(track)):
        if track[i][CURRENT_TIME] < L:
            if i == 0:
                current_time = track[0][CURRENT_TIME] 
            else:
                current_time += track[i][CURRENT_TIME] - track[i-1][CURRENT_TIME]
            cycle = track[i][RED_LIGTH_TIME] + track[i][GREEN_LIGHT_TIME]
            red_light = current_time % cycle < track[i][RED_LIGTH_TIME]
            if red_light:
                waiting_time = track[i][RED_LIGTH_TIME] - current_time % cycle 
                current_time += waiting_time
            last_light_index = i
        else:
            break
    if current_time:
        current_time += L - track[last_light_index][CURRENT_TIME]
    else:
        current_time = L
    
    return current_time