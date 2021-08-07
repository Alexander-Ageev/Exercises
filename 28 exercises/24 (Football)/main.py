def get_unsorted_index(array):
    indices_of_unordered_numbers_array = []
    sort_array = sorted(array)
    for i in range(len(array)):
        if array[i] != sort_array[i]:
            indices_of_unordered_numbers_array.append(i)
    return indices_of_unordered_numbers_array

def check_sequence(indices_array):
    for i in range(len(indices_array) - 1):
        if indices_array[i+1] - indices_array[i] > 1:
            return False
    return True

def Football(source_array, N):
    indices_to_sort = get_unsorted_index(source_array)
    if len(indices_to_sort) == 0:
        result = False
    elif len(indices_to_sort) == 2:
        result = True
    elif check_sequence(indices_to_sort):
        result = True
    else:
        result = False
    return result
