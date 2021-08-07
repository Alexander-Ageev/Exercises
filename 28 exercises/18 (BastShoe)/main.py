index = 0
Task_Queue = [] # list of (command, data)


def queue_processing():
    result = ''
    for i in range(index):
        if Task_Queue[i][0] == '1':
            result += Task_Queue[i][1]
        elif Task_Queue[i][0] == '2':
            if len(result) > int(Task_Queue[i][1]):
                result = result [0: len(result) - int(Task_Queue[i][1])]
            else:
                result = ''
    return result

def BastShoe(command):
    global index, Task_Queue
    key = command[0]
    data = command[2:]
    if key == '1' and index == len(Task_Queue): # add operation, no undo operations
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == '2' and index == len(Task_Queue): # delete operation, no undo
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif index < len(Task_Queue) and key in ['1', '2']: # undo operations apply
        Task_Queue = [ ('1', queue_processing()) ]
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
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
        if index < len(Task_Queue):
            index += 1
        else:
            index = len(Task_Queue)
    result = queue_processing()
    return result