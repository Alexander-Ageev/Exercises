def my_sort(N, Tele):
    sort_count = 1
    while sort_count:
        sort_count = 0
        for i in range(N-1):
            if Tele[i] > Tele[i+1]:
                Tele[i], Tele[i+1] = Tele[i+1], Tele[i]
                sort_count += 1
    return Tele

def MadMax(N, Tele):
    if len(Tele) == 1:
        return Tele
    else:
        Tele = my_sort(N, Tele)
        tele_min = Tele[0 : N//2]
        tele_max = Tele[:N//2-1: -1]
        result = tele_min + tele_max
        return result