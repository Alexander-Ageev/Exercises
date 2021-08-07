import datetime as dt
mode = ['one-time', 'weekly', 'monthly', 'yearly']

class Alarm:
    def __init__(self, name = 'Новый будильник', en = True, time = dt.time(12, 0), mode = 'one-time', day_of_week = [False for i in range(7)], message = ''):
        self.name = name # название будильника
        self.enable = en # включен ди будильник
        self.time = time # время срабатывания
        self.mode = mode # режим работы: разовое/периодическое срабатывание
        self.day_of_week = day_of_week # дни недели работы будильника
        self.message = message # сообщение, которое выводит будильник
        
        # Мы можем включать и выключать будильник, не заходя в настройки.
    def enable (self):
        self.enable = True
    def disable (self):
        self.enable = False
        
    # Мне кажется, перезаписывать параметры будильника по отдельности не очень правильно.
    # Лучше создать форму с настройками, на которую будут выведены настройки по умолчанию или
    # предыдущие настройки, изменить что нужно, подтвердить изменения и вызвать метод change
    def change (self, name, en, time, mode, day_of_week, message):
        self.name = name
        self.enable = en
        self.time = time
        self.mode = mode
        self.day_of_week = day_of_week
        self.message = message
        
    def horn (self):
        # Тут должен быть код, который читает звуковой файл и выводит его на динамик,
        # либо звук может синтезироваться генератором сигнала заданной частоты и длительности.
        print(self.message)
        
        
    def check (self, now):
        if self.enable == True:
            if self.day_of_week[now.weekday()] == True or sum(self.day_of_week) == 0:
                if self.time == now.time():
                    print(now.strftime("%d-%m %H:%M"))
                    self.horn()
                    if self.mode == 'one-time':
                        self.disable()
    
    # Деструктор в материалах не описан, но я на свой страх и риск попробовал его описать.
    def __del__ (self):
        print(f'{self.name}, больше ты меня никогда не разбудишь!')
    
class Calendar:
    def __init__ (self, date, message, name = 'Новое событие', mode = 'one_time'):
        self.name = name
        self.date = date
        self.mode = mode # один раз/еженедельно/ежемесячно/ежегодно
        self.message = message
        self.date_reached = False
    
    def display(self, now):
        if self.date.date() == now.date():
            print(f'{self.message}\t{now.strftime("%d-%m-%Y")}') # Выводим сообщение на экран в течение всего дня
            self.date_reached = True
        elif self.date_reached == True:
            self.date_reached = False
            if self.mode == 'weekly':
                self.date += dt.timedelta(days=7)
            elif self.mode == 'monthly':
                m = self.date.month + 1
                if m // 12 == 0 or m % 12 == 0: # Когда нет переполнения month
                    self.date = self.date.replace(month=m)
                else:
                    y = self.date.year + 1
                    m = (self.date.month + 1) % 12
                    self.date = self.date.replace(year = y, month = m)
            elif self.mode == 'yearly':
                y = self.date.year + 1
                self.date = self.date.replace(year = y)
        else:
            self.date_reached = False
        
    def change (self, date, message, name, mode):
        self.name = name
        self.date = date
        self.mode = mode # один раз/еженедельно/ежемесячно/ежегодно
        self.message = message        
        

date = dt.datetime (2021, 2, 23)
event = Calendar(date, 'День защитника отечества')
event_name = event.name
event_date = event.date
event_message = event.message
event_mode = mode[3]
event.change(event_date, event_message, event_name, event_mode)
#print(f'{event.name}\n{event.date}\n{event.mode}\n{event.message}\n')

Al1 = Alarm()
# На интерфейсе всплывает окно настроек будильника_1, меняем их
# Переменные current_var - соответствующие поля на интерфейсе
current_name = 'Завтрак'
current_enable = Al1.enable # это значение не было изменено
current_time = dt.time(8, 0)
current_mode = 'сontinuous'
current_day_of_week = [True for i in range(7)]
current_message = 'Эй, проснись! Ну ты и соня. Тебя даже вчерашний шторм не разбудил.'
# Подтвердили настройки будильника_1
Al1.change (current_name, current_enable, current_time, current_mode, current_day_of_week, current_message)
#print(f'{Al1.name}\n{Al1.enable}\n{Al1.time}\n{Al1.mode}\n{Al1.day_of_week}\n')

Al2 = Alarm()
# На интерфейсе всплывает окно настроек будильника_2, меняем их
current_name = 'Кино'
current_enable = Al2.enable # это значение не было изменено
current_time = dt.time(20, 0)
current_mode = Al2.mode # это значение не было изменено
current_day_of_week = Al2.day_of_week # это значение не было изменено
current_message = 'Время смотреть кино'
# Подтвердили настройки будильника_2
Al2.change (current_name, current_enable, current_time, current_mode, current_day_of_week, current_message)
#print(f'{Al2.name}\n{Al2.enable}\n{Al2.time}\n{Al2.mode}\n{Al2.day_of_week}\n')

#Тесты
now_time = dt.datetime (2021, 2, 22, 0, 0, 0)
time_offset = dt.timedelta (hours = 1)
for i in range(60):
    now_time += time_offset
    Al1.check(now_time)
    Al2.check(now_time)
    event.display(now_time)
# А тут наш соня не выдержал
del Al1



