6.1. Разберите свой код, и сделайте пять примеров, где можно более наглядно учесть в именах переменных уровни абстракции.
# merge_items - функция объединения данных об одинаковых товарах,
# переменная item_name_count_array более точно отражает информацию о содержании данных, по которым происходит объединение
def merge_items(item_name_count_array):
    db = {}
    for i in range(len(item_name_count_array)):
        item_name_count = item_name_count_array[i].split()
        if item_name_count[0] in db:
            db[item_name_count[0]] += int(item_name_count[1])
        else:
            db[item_name_count[0]] = int(item_name_count[1])
    grouped_items_array = list(db.items())
    return grouped_items_array
 #items_array - поскольку ShopOLAP - main-функция, имя переменной логично сделать 
 # наиболее приближенным к логике выполнения, а обозначение array позволяет помнить о типе данных
 # Объединение списка и сортировка - основные требования к функции, поэтому обозначены соответствующие переменные
def ShopOLAP(N, items_array):  
    merged_items = merge_items(items_array)
    sorted_items = sort_items_for_count(merged_items)
    sales_report = sort_items_for_name(sorted_items)
    return sales_report
///////////////////////////////////////////////////////////////////
# Имена переменных имеют смысл и прямое отношение к поставленной задаче
def Keymaker(number_of_doors):
    state_of_doors = ['0' for i in range(number_of_doors)]        
    i = 0
    while (i+1) ** 2  <= number_of_doors:
        state_of_doors[(i+1) ** 2 - 1] = '1'
        i += 1
    result_sate_of_doors = ''.join(state_of_doors)
    return result_sate_of_doors
///////////////////////////////////////////////////////////////////
# Функция проверяет порядок следования чисел в массиве
def get_unsorted_index(array):
    indices_of_unordered_array = []
    sort_array = sorted(array)
    for i in range(len(array)):
        if array[i] != sort_array[i]:
            indices_of_unordered_array.append(i)
    return indices_of_unordered_array
# Функция проверяет порядок следования индексов
def check_sequence(indices_array):
    for i in range(len(indices_array) - 1):
        if indices_array[i+1] - indices_array[i] > 1:
            return False
    return True
# Main-функция, имена переменных наиболее близки к контексту
def Football(fotballer_position, N):
    footballer_to_relocation = get_unsorted_index(fotballer_position)
    if len(footballer_to_relocation) == 0:
        result = False
    elif len(footballer_to_relocation) == 2:
        result = True
    elif check_sequence(footballer_to_relocation):
        result = True
    else:
        result = False
    return result
///////////////////////////////////////////////////////////////////
def split_string(s): # s - source_string
    text = [] # strings
    numbers = []
    temp_str = '' # temp_strings
    for char in s:
        if char.isdigit():
            numbers.append(int(char))
            text.append(temp_str)
            temp_str = ''
        else:
            temp_str += char
    text.append(temp_str)
    return [text, numbers]
# Имена переменных подобраны плохо, слишком короткие
def find_symbol(s, sym): # s - source_string, sym - search_char
    count = 0 # char_count
    while sym in s:
        count += 1
        s = s[s.find(sym)+1:]
    return count
# В данной функции имена переменных подобраны не лучшим образом. Приходится по несколько раз просматривать код, чтобы понять суть  
def white_walkers(village):
    temp = split_string(village)
    numbers = temp[1] # citizens_array
    text = temp[0] # fields_array
    walkers = 0 # walkers_count
    citizens = 0 # citizens_count
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i+1] == 10:
            citizens +=1
            if find_symbol(text[i+1], '=') == 3:
                walkers += 1
    if citizens == walkers and citizens > 0:
        return True
    else:
        return False
///////////////////////////////////////////////////////////////////
RING_BUFFER = 3
# нарушение уровня абстракции: имена используемых переменных имеют прямое отношение к функции более высокого уровня
def do_first (a, partition): # a - first_number_dest, partition - number_sequence
    step = 0 # step - i, переменная step может сбить с толку, есть стандартное обозначение переменной-счетчика итераций
    while partition[0] != a and step <= RING_BUFFER:
        temp = partition[0]  
        for i in range(RING_BUFFER-1):
            partition[i] = partition[i+1]
        partition[-1] = temp
    return partition

def MisterRobot(N, data):
    result = True
    for i in range(N):
        current_number = i+1
        current_number_index = data.index(current_number)
        if i != current_number_index:
            while data.index(current_number) != i:
                current_number_index = data.index(current_number)
                if current_number_index - (i - 1) < RING_BUFFER:
                    start = i                   # start_index
                    stop = i + RING_BUFFER      # stop_index
                else:
                    start = current_number_index - RING_BUFFER + 1                    
                    stop = current_number_index + 1
                try:
                    partition = do_first(current_number, data[start: stop])
                    data[start: stop] = partition
                except:
                    result = False
                    break
    return result


6.2. Приведите четыре примера, где вы в качестве имён переменных использовали или могли бы использовать технические термины из информатики.
        В задании BastShoe переменную queue можно заменить на JobQueue
        имя_переменной_index для обозначения порядкового номера элемента массива (например, в задании MisterRobot, Unmanned, Footbal)
        имя_переменной_array для обозначения набора однотипных данных (ShopOLAP, Footbal, и т.д.)
        matrix - для обозначения двумерного массива, состоящего из чисел
        bin/oct/hex для обозначения данных, используемых в соответствующей системе счисления

6.3. Придумайте или найдите в своём коде три примера, когда имена переменных даны с учётом контекста (функции, метода, класса).
# Функция вычисляет размер матрицы в зависимости от длины строки s. Имена переменных в данной функции вписываются в контекст работы с матрицами
def matrix_size(s):
    size = []
    n = len(s) ** 0.5
    row = int(n)
    column = int(n + 0.5)
    if row * column < len(s):
        size.extend([row+1, column])
    else:
        size.extend([row, column])
    return size
///////////////////////////////////////////////////////////////////
def white_walkers(village):
    temp = split_string(village)
    citizens = temp[1]
    fields = temp[0]
    walkers_count = 0
    citizens_count = 0
    for i in range(len(citizens) - 1):
        if citizens[i] + citizens[i+1] == 10:
            citizens_count +=1
            if find_walkers(citizens[i+1], '=') == 3:
                walkers_count += 1
    if citizens_count == walkers_count and citizens_count > 0:
        return True
    else:
        return False
///////////////////////////////////////////////////////////////////
class Tree(object):
    # Create matrix H*W, where 0 - none, n - age of branches
    def __init__ (self, H, W, tree):
        self.heigh = H
        self.width = W
        self.age = 0
        result = []
        for i in tree:
            line = []
            for j in i:
                if j == '.':
                    line.append(0)
                elif j == '+':
                    line.append(1)
            result.append(line)
        self.state = result

6.4. Найдите пять имён переменных в своём коде, длины которых не укладываются в 8-20 символов, и исправьте, 
чтобы они укладывались в данный диапазон.
indices_of_unordered_numbers_array - unordered_num_indices
text - field_array
A - input_sequence
B - result_sequence
number_max_votes_candidate - num_max_votes_personi