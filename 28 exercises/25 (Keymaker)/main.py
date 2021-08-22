CLOSE_DOOR = '0'
OPEN_DOOR = '1'

def Keymaker(doors_count):
    state_of_doors = [CLOSE_DOOR for i in range(doors_count)]        
    door_index = 0
    while (door_index+1) ** 2  <= doors_count:
        state_of_doors[(door_index+1) ** 2 - 1] = OPEN_DOOR
        door_index += 1
    result_sate_of_doors = ''.join(state_of_doors)
    return result_sate_of_doors

