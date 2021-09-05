import random
HOME = 'C:\\Temp\\'

sum = 0
no_error = True

for i in range(2):
    filename = HOME + str(random.randint(1, 2)) + '.txt'
    with open(filename, 'rt') as file:
        for j in range(3):
            s = file.readline().rstrip()
            if s != '':
                try:
                    sum += int(s)
                except:
                    print(f'Содержимое файла {filename} не является числом')
                    no_error = False
                    break    
                
            else:
                print(f'Содержимое файла {filename} неполное')
                no_error = False
                break
        file.close()
if no_error:
    print(f'Сумма чисел в файлах: {sum}')
