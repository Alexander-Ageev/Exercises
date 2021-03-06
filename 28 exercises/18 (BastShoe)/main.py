ADD_COMMAND = '1'
DELETE_COMMAND = '2'
GET_CHAR_COMMAND = '3'
UNDO_COMMAND = '4'
REDO_COMMAND = '5'

index = 0
Task_Queue = [] # list of (command_string, data_string)

def queue_processing():
    result = ''
    for i in range(index):
        if Task_Queue[i][0] == ADD_COMMAND:
            result += Task_Queue[i][1]
        elif Task_Queue[i][0] == DELETE_COMMAND:
            queue_not_empty = len(result) > int(Task_Queue[i][1])
            if queue_not_empty:
                result = result [0: len(result) - int(Task_Queue[i][1])]
            else:
                result = ''
    return result

def BastShoe(command):
    global index, Task_Queue
    key = command[0]
    data = command[2:]
    undo = index != len(Task_Queue)
    if key == ADD_COMMAND and not undo:
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == DELETE_COMMAND and not undo:
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif undo and key in [ADD_COMMAND, DELETE_COMMAND]:
        Task_Queue = [ (ADD_COMMAND, queue_processing()) ]
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == GET_CHAR_COMMAND:
        result = queue_processing()    
        try:
            result = result[int(data)]
        except:
            result = ''
        return result
    elif key == UNDO_COMMAND:
        if index > 1:
            index -= 1
        else:
            index = 1
    elif key == REDO_COMMAND:
        if index < len(Task_Queue):
            index += 1
        else:
            index = len(Task_Queue)
    result = queue_processing()
    return result