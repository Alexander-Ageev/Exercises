ADD_COMAND = '1'
DELETE_COMAND = '2'
GET_CHAR_COMAND = '3'
UNDO_COMAND = '4'
REDO_COMAND = '5'

index = 0
Task_Queue = [] # list of (command, data)

def queue_processing():
    result = ''
    for i in range(index):
        if Task_Queue[i][0] == ADD_COMAND:
            result += Task_Queue[i][1]
        elif Task_Queue[i][0] == DELETE_COMAND:
            if len(result) > int(Task_Queue[i][1]):
                result = result [0: len(result) - int(Task_Queue[i][1])]
            else:
                result = ''
    return result

def BastShoe(command):
    global index, Task_Queue
    key = command[0]
    data = command[2:]
    if key == ADD_COMAND and index == len(Task_Queue): # add operation, no undo operations
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == DELETE_COMAND and index == len(Task_Queue): # delete operation, no undo
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif index < len(Task_Queue) and key in [ADD_COMAND, DELETE_COMAND]: # undo operations apply
        Task_Queue = [ (ADD_COMAND, queue_processing()) ]
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == GET_CHAR_COMAND: # get text[index]
        result = queue_processing()    
        try:
            result = result[int(data)]
        except:
            result = ''
        return result
    elif key == UNDO_COMAND:
        if index > 1:
            index -= 1
        else:
            index = 1
    elif key == REDO_COMAND:
        if index < len(Task_Queue):
            index += 1
        else:
            index = len(Task_Queue)
    result = queue_processing()
    return result