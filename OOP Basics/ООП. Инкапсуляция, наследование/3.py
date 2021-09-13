import datetime as dt
period = ['one-time', 'weekly', 'monthly', 'yearly']


class time_apps:
    def __init__ (self, datetime, message, name, mode):
         self._datetime = datetime 
         self._message = message 
         self._name = name 
         self._mode = mode 

    def get_datetime(self):
        return self._datetime
    def get_message(self):
        return self._message
    def get_name(self):
        return self._name
    def get_mode(self):
        return self._mode

class Alarm(time_apps):
    def __init__(self, datetime = dt.time(12, 0), message = '', name = 'Новый будильник', 
    mode = period[0], en = True, day_of_week_enable = [False for i in range(7)]):
        super().__init__(datetime, message, name, mode)
        self.__enable = en 
        self.__day_of_week = day_of_week_enable

    def get_day_of_week(self):
        return self.__day_of_week
    def get_enable(self):
        return self.__enable

    def enable (self):
        self.__enable = True
    def disable (self):
        self.__enable = False
         
    def change (self, name, en, time, mode, day_of_week, message):
        self._name = name
        self.__enable = en
        self._datetime = time
        self._mode = mode
        self.__day_of_week = day_of_week
        self._message = message
        
    def horn (self):
        # Тут должен быть код, который читает звуковой файл и выводит его на динамик,
        # либо звук может синтезироваться генератором сигнала заданной частоты и длительности.
        print(self._message)
       
    def check (self, now):
        if self.__enable and (self.__day_of_week[now.weekday()] or sum(self.__day_of_week) == 0) 
        and self._datetime == now.time():
            print(now.strftime("%d-%m %H:%M"))
            self.horn()
            if self._mode == 'one-time':
                self.disable()

    def print_info (self):
        print(f'{self._name}\n{self.__enable}\n{self._datetime}\n{self._mode}\n{self.__day_of_week}\n')

    
class Calendar(time_apps):
    def __init__ (self, datetime, message, name = 'Новое событие', mode = period[0]):
        super().__init__(datetime, message, name, mode)

    def change (self, date, message, name, mode):
        self._name = name
        self._datetime = date
        self._mode = mode # один раз/еженедельно/ежемесячно/ежегодно
        self._message = message        

# Когда наступает дата, в течение всего дня выводится сообщение на экран.
# После окончания даты она переносится на указанный период
    def display_opt (self, now):
        if self._datetime.date() == now.date():
            print(f'{self._message}\t{now.strftime("%d-%m-%Y")}')
        elif self._datetime.date() < now.date():
            self.__date_modify()
# данный метод не обрабатывает случай, когда _datetime.data отличается от now.date больше, чем на один период
    def __date_modify (self):
        if self._mode == 'weekly':
            self._datetime += dt.timedelta(days = 7)
        elif self._mode == 'monthly':
                if self._datetime.month == 12: # Когда нет переполнения month                          
                    self._datetime = self._datetime.replace(year = self._datetime.year + 1, month = 1)                    
                else:                    
                    self._datetime = self._datetime.replace(month = self._datetime.month + 1)                    
        elif self._mode == 'yearly':
            self._datetime = self._datetime.replace(year = self._datetime.year + 1)

date = dt.datetime (2021, 2, 23)
event = Calendar(date, 'День защитника отечества')
event_name = event.get_name()
event_date = event.get_datetime()
event_message = event.get_message()
event_mode = period[2]
event.change(event_date, event_message, event_name, event_mode)

Al1 = Alarm()
# На интерфейсе всплывает окно настроек будильника_1, меняем их
# Переменные current_var - соответствующие поля на интерфейсе
current_name = 'Завтрак'
current_enable = Al1.get_enable() # это значение не было изменено
current_time = dt.time(8, 0)
current_mode = 'сontinuous'
current_day_of_week = [True for i in range(7)]
current_message = 'Эй, проснись! Ну ты и соня. Тебя даже вчерашний шторм не разбудил.'
# Подтвердили настройки будильника_1
Al1.change (current_name, current_enable, current_time, current_mode, current_day_of_week, current_message)
Al1.print_info()

Al2 = Alarm()
# На интерфейсе всплывает окно настроек будильника_2, меняем их
current_name = 'Кино'
current_enable = Al2.get_enable() # это значение не было изменено
current_time = dt.time(20, 0)
current_mode = Al2.get_mode() # это значение не было изменено
current_day_of_week = Al2.get_day_of_week() # это значение не было изменено
current_message = 'Время смотреть кино'
# Подтвердили настройки будильника_2
Al2.change (current_name, current_enable, current_time, current_mode, current_day_of_week, current_message)


#Тесты
now_time = dt.datetime (2021, 2, 22, 0, 0, 0)
time_offset = dt.timedelta (days = 1)
for i in range(60):
    now_time += time_offset
    Al1.check(now_time)
    Al2.check(now_time)
    event.display_opt(now_time)


