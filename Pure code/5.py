3.1. Улучшите пять имён классов в вашем коде.
Tree # Имя класса, точно описывающее суть задачи tree_of_life
time_apps - date_time_applications # Имя родительского класса для классов будильник и календарь
Alarm # Имя класса для объектов "будильник"
Calendar # Имя класса для объектов "событие"
figure # Имя родительского класса геометрических фигур
triangle # Имя класса для объектов "треугольник"
circle # Имя класса для объектов "круг"
error # Имя класса дляобъектов "ошибка"
people # Имя класса для объектов "люди"
# Это все использованные мной классы. Дать более точные имена сложно - недостаточно контекста в задачах

3.2. Улучшите семь имён методов и объектов по схеме из пункта 2.
Al1, Al2 # Объект класса Alarm. Будильнику сложно заранее присвоить осмысленное имя. 
#В идеальной ситуации стоит динамически создавать объекты с именем = Al_'%alarm.name' (при этом возникает сложность с именем будильника на любом языке, кроме английского)
event # объект класса Calendar; аналогично будильнику - самое осмысленное имя получилось бы ev_'%Calendar.name'
display_opt - display_message # метод класса Calendar; непонятно что имелось ввиду в первом случае, message - существующее поле, которое и выводится
# остальные методы соответсвуют концепции "похожие действия - одно название метода"
# например, get/set, mode, enable, name, message, check