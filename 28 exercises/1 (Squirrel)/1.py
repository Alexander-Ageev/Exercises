def squirrel(N):
    nuts = 0
    for i in range(N+1):
        if i == 0:
            nuts = 1
        else:
            nuts *= i
    emeralds_s = str(nuts)[0]
    emeralds = int(emeralds_s)
    return emeralds