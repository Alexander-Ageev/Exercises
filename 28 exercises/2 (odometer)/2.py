def odometer (oksana):
    speed = oksana[::2]
    time = [0]
    time += oksana[1::2]
    distance = 0
    for i in range(len(speed)):
        distance += speed[i] * (time[i+1] - time[i])
    return distance