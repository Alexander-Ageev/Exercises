#Задание 2.
import datetime as dt

class Alarm:
    name = 'new Alarm' # название будильника
    enable = True  # включен ди будильник
    time = dt.time(12, 0) # время срабатывания
    mode = 'one-time' # режим работы: разовое/периодическое срабатывание
    day_of_week = [
        False,# Понедельник
        False,# Вторник
        False,# Среда
        False,# Четверг
        False,# Пятница
        False,# Суббота
        False,# Воскресенье
    ]
    message = ''

class Calendar:
    name = ''
    date = dt.datetime.utcnow
    mode = 'yearly' # один раз/ежемесячно/ежегодно


date1 = Calendar()
date1.name = 'New Year'
date1.date = dt.date(2022, 1, 1)
print(f'{date1.name}\n'
      f'{date1.date}\n'
)

Al1 = Alarm()
Al1.name = 'Breakfast'
Al1.time = dt.timedelta (hours =  8, minutes = 00)
Al1.mode = 'сontinuous'
Al1.day_of_week = [True for i in range(7)]
print(f'{Al1.name}\n' +
      f'{Al1.enable}\n' +
      f'{Al1.time}\n' +
      f'{Al1.mode}\n' +
      f'{Al1.day_of_week}\n'\
       )

Al2 = Alarm()
Al2.name = 'Cinema'
Al2.time = dt.timedelta (hours =  19, minutes = 50)
Al2.message = 'Go to TV'
print(f'{Al2.name}\n' +
      f'{Al2.enable}\n' +
      f'{Al2.time}\n' +
      f'{Al2.mode}\n' +
      f'{Al2.day_of_week}\n'\
       )

# Задание 3
# Данный блок кода показывает особенность передачи объекта по ссылке. Думаем, 
#что скопировали объект и внесли небольше изменения, а на самом деле - 
# скопировали ссылку на объект и изменили данные объекта Al1
Al3 = Al1
Al3.name = 'Lunch'
Al3.time = dt.timedelta (hours =  14, minutes = 00)
print('Задание 3')
print(f'{Al3.name}\n' +
      f'{Al3.time}\n' +
      f'{Al3.day_of_week}\n'\
       )
print(f'{Al1.name}\n' +
      f'{Al1.time}\n' +
      f'{Al1.day_of_week}\n'\
       )


