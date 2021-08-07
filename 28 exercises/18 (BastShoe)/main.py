index = 0
queue = [] # list of (command, data)


def queue_processing():
    result = ''
    for i in range(index):
        if queue[i][0] == '1':
            result += queue[i][1]
        elif queue[i][0] == '2':
            if len(result) > int(queue[i][1]):
                result = result [0: len(result) - int(queue[i][1])]
            else:
                result = ''
    return result

def BastShoe(command):
    global index, queue
    key = command[0]
    data = command[2:]
    if key == '1' and index == len(queue): # add operation, no undo operations
        queue.append( (key, data) )
        index = len(queue)
    elif key == '2' and index == len(queue): # delete operation, no undo
        queue.append( (key, data) )
        index = len(queue)
    elif index < len(queue) and key in ['1', '2']: # undo operations apply
        queue = [ ('1', queue_processing()) ]
        queue.append( (key, data) )
        index = len(queue)
    elif key == '3': # get text[index]
        result = queue_processing()    
        try:
            result = result[int(data)]
        except:
            result = ''
        return result
    elif key == '4': # undo
        if index > 1:
            index -= 1
        else:
            index = 1
    elif key == '5': #redo
        if index < len(queue):
            index += 1
        else:
            index = len(queue)
    result = queue_processing()
    return result