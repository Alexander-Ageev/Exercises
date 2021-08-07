def squirrel(N):
    nuts = 0
    for i in range(N+1):
        if i == 0:
            nuts = 1
        else:
            nuts *= i
    first_char = str(nuts)[0]
    emeralds = int(first_char)
    return emeralds