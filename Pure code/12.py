# Связывание в коде. BigMinus. В данном случае происходит вычитание одного числа из другого. 
# Данный фрагмент отвечает за обработку результата: удаление лишних нулей перед числом и работу с отрицательными числами. 
# Данные операции с числами не предполагают вариативность констант
def result_verification(input_list, length_string):
    input_string = input_list[0]
    negative = input_list[1]
    result_string = input_string.lstrip('0')
    if result_string == '':
        result_string = '0'
    if negative:
        s1 = result_string
        s2 = '1' + '0' * length_string
        result_string = BigMinus(s2, s1)
    return result_string  

# Связывание при компилляции. BastShoe. В данном случае значения команд 
# присваиваются через константу в первую очередь для удобства восприятия кода, 
# при этом таже сохраняется возможность изменения и/или дополнения списка команд
ADD_COMMAND = '1'
DELETE_COMMAND = '2'
GET_CHAR_COMMAND = '3'
UNDO_COMMAND = '4'
REDO_COMMAND = '5'

index = 0
Task_Queue = [] # list of (command, data)

def queue_processing():
    result = ''
    for i in range(index):
        if Task_Queue[i][0] == ADD_COMMAND:
            result += Task_Queue[i][1]
        elif Task_Queue[i][0] == DELETE_COMMAND:

# Связывание на этапе выполнения. Задание на работу с файлами в курсе основы ООП.
# В качестве параметра на этапе выполнения выступают строки данных в файле. 
filename = f"{HOME}data.txt"
with open(filename, 'rt', encoding='utf-8') as file:
    string = file.readline()
    string.rstrip('\n')
    string_number = 0
    while string:
        data = string.split('\t')