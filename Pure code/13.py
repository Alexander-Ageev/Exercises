# Данный код лучше заменить
    size = matrix_size(s)
    row = size[0]
    column = size[1]
# на 
    row, column = matrix_size(s)

# В Данном фрагменте можно было бы использовать очередь
for i in range(len(track)):
        if track[i][0] < L:
            if i == 0:
                current_time = track[0][0] 
            else:
                current_time += track[i][0] - track[i-1][0]
            cycle = track[i][1] + track[i][2]
            red_light = current_time % cycle < track[i][1]
            if red_light:
                waiting_time = track[i][1] - current_time % cycle 
                current_time += waiting_time
            last_light_index = i
        else:
            break

# Тут можно было бы испльзовать очередь
for i in range(N-1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sort_count += 1

# списковую переменную item_data стоит рабить на две переменные: item_name и item_count
# item_name, item_count = item_data
for i in range(len(item_data_array)):
        item_data = item_data_array[i].split()
        if item_data[0] in db:
            db[item_data[0]] += int(item_data[1])
        else:
            db[item_data[0]] = int(item_data[1])

# Остальной код либо работает с матрицами, либо достаточно прозрачный, чтобы усложнять его очередями или иными структурами данных