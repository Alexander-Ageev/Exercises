HOME = 'C:\\Temp\\'

class error:
    def __init__(self, name, source, type_er):
        self.__name = name
        self.__source = source
        self.__type = type_er
    def get_data (self):
        return f'{self.__name}\t{self.__source}\t{self.__type}'

class people:
    def __init__(self):
        self.__error = []

    def set_name(self, name):
        if name:
            self.__name = name
        else:
            self.__name = 'invalid_name'
            self.__error.append(error(self.__name, 'name', 'invalid name'))
    def set_age(self, age):            
        try:
            self.__age = int(age)
            if self.__age < 0 or self.__age > 150:
                self.__error.append(error(self.__name, 'age', 'invalid age'))
        except:
            self.__error.append(error(self.__name, 'age', 'invalid datatype'))
    def set_growth(self, growth):
        try:
            self.__growth = int(growth)
            if self.__growth <= 0 or self.__growth > 300:
                self.__error.append(error(self.__name, 'growth', 'invalid growth'))
        except:
            self.__error.append(error(self.__name, 'growth', 'invalid datatype'))
    def set_weight(self, weight):
        try:
            self.__weight = int(weight)
            if self.__weight <= 0 or self.__weight > 500:
                self.__error.append(error(self.__name, 'weight', 'invalid weight'))
        except:
            self.__error.append(error(self.__name, 'weight', 'invalid datatype'))
    def get_data (self):
        data = f'{self.__name}\t{self.__age}\t{self.__growth}\t{self.__weight}'
        return data
    def check_error(self):
        if self.__error:
            for i in range(len(self.__error)):
                print(self.__error[i].get_data())
            return i+1
        else:
            return 0

peoples = []
data = []
filename = f"{HOME}data.txt"
with open(filename, 'rt', encoding='utf-8') as file:
    string = file.readline()
    string.rstrip('\n')
    string_number = 0
    while string:
        data = string.split('\t')
        if len(data) == 4:
            person = people()
            person.set_name(data[0])
            person.set_age(data[1])
            person.set_growth(data[2])
            person.set_weight(data[3])
            if person.check_error() == 0:
                peoples.append(person)
        else:
            print(f'Некорректный формат строки №{string_number}')
        string = file.readline()
        string.rstrip('\n')
        string_number += 1
    file.close()

print('\nСписок людей:')
for i in range(len(peoples)):
    print(peoples[i].get_data())