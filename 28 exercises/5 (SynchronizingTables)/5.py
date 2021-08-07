def  my_sort(N, array):
    sort_count = 1
    while sort_count:
        sort_count = 0
        for i in range(N-1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort_count += 1
    return array

def SynchronizingTables(N, ids, salary):
    ids_array = list(ids)
    result = [0 for i in range(N)]
    sorted_salary = my_sort(N, salary)
    for i in range(N):
        max_index = i
        max = ids_array[i]
        for j  in range(N):
            if ids_array[j] >= max:
                max = ids_array[j]
                max_index = j
        ids_array[max_index] = 0
        result[max_index] = sorted_salary[i]
    return result