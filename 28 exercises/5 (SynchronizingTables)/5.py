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
    temp = list(ids)
    result = [0 for i in range(N)]
    sorted_salary = my_sort(N, salary)
    for i in range(N):
        index = i
        max = temp[i]
        for j  in range(N):
            if temp[j] >= max:
                max = temp[j]
                index = j
        temp[index] = 0
        result[index] = sorted_salary[i]
    return result