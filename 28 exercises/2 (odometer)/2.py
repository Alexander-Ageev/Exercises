# oksana - list of the [speed(1), time(1), speed(2), time(1 + 2) ..., speed(n), time(1 + 2 + ... + n)]
def odometer (oksana):
    speed = oksana[::2]
    time = [0]
    time += oksana[1::2]
    distance = 0
    for i in range(len(speed)):
        distance += speed[i] * (time[i+1] - time[i])
    return distance