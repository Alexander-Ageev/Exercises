// п. 13. Заменил комментарий на константу
expense += 23 # for another char
expense += ANOTHER_CHAR_COST

// п.4. Избыточный комментарий, удалил
    elif key == GET_CHAR_COMMAND: # get text[index]
        result = queue_processing()    
        try:
            result = result[int(data)]

// п. 13 и п. 4. Добавил более удобочитаемую переменную, комментарии стали избыточны, удалил их
no_undo_operations = index == len(Task_Queue)
    if key == ADD_COMMAND and no_undo_operations: # add operation, no undo operations
        Task_Queue.append( (key, data) )
        index = len(Task_Queue)
    elif key == DELETE_COMMAND and no_undo_operations: # delete operation, no undo

// п.3. В комментарии не был описан тип данных в списке, добавил _string
Task_Queue = [] # list of (command_string, data_string)

// п. 13. Добавил константы, удалил комментарий
CURRENT_TIME = 0
RED_LIGTH_TIME = 1
GREEN_LIGHT_TIME = 2
# track - list of the [current_time, time_red_i, time_green_i]
def Unmanned(L, N, track):
     cycle = track[i][RED_LIGTH_TIME] + track[i][GREEN_LIGHT_TIME]

// п. 4, удалил. Также удалил из этого кода еще несколько комментариев на предыдущем занятии
REMOVE_BRANCH_TEMPLATE = [(-1, 0), (0, 1), (1, 0), (0, -1)] # Map of the clear branches

// п.4, удалил
# Функция создана для удобства, чтобы не создавать и не удалять файл каждый раз
def create_doc(path, text):
    if os.path.isfile(path):
        # Если файл создан, удаляем его
        os.remove(path)
    # Если файла нет или он удален, создаем новый с известным соержимым
    doc = Document()

// п.4. Удалил комментарии
 def __init__ (self, datetime, message, name, mode):
         self._datetime = datetime # время срабатывания         
         self._message = message # сообщение, которое выводит будильник
         self._name = name # название будильника
         self._mode = mode # режим работы: разовое/периодическое срабатывание 

// п. 12. Удалил
#    print(now_time)

// п. 9. Удалил.
    # Мне кажется, перезаписывать параметры будильника по отдельности не очень правильно.
    # Лучше создать форму с настройками, на которую будут выведены настройки по умолчанию или
    # предыдущие настройки, изменить что нужно, подтвердить изменения и вызвать метод change

// п.4. Удалил
        assert self.__hight != 0 # проверка нужна для исключения работы с некорректными размерами фигуры

// В процессе прохождения курса Ясный Код я подчищал откровенно ненужные комментарии. 
// В основном это были комментарии из п.4, п.13 и п.8