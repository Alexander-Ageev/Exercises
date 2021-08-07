def Keymaker(number_of_doors):
    state_of_doors = ['0' for i in range(number_of_doors)]        
    i = 0
    while (i+1) ** 2  <= number_of_doors:
        state_of_doors[(i+1) ** 2 - 1] = '1'
        i += 1
    result_sate_of_doors = ''.join(state_of_doors)
    return result_sate_of_doors

