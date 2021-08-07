RING_BUFFER = 3

def do_first (a, partition):
    step = 0
    while partition[0] != a and step <= RING_BUFFER:
        temp = partition[0]  
        for i in range(RING_BUFFER-1):
            partition[i] = partition[i+1]
        partition[-1] = temp
    return partition


def MisterRobot(N, data):
    data_may_be_ordered = True
    for i in range(N):
        current_number = i+1
        current_number_index = data.index(current_number)
        if i != current_number_index:
            while data.index(current_number) != i:
                current_number_index = data.index(current_number)
                if current_number_index - (i - 1) < RING_BUFFER:
                    start = i
                    stop = i + RING_BUFFER
                else:
                    start = current_number_index - RING_BUFFER + 1                    
                    stop = current_number_index + 1
                try:
                    partition = do_first(current_number, data[start: stop])
                    data[start: stop] = partition
                except:
                    data_may_be_ordered = False
                    break
    return data_may_be_ordered