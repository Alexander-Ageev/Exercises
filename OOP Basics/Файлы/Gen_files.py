import random
HOME = 'C:\\Temp\\'

for i in range(1, 11):
    data = ''
    for j in range(3):
        data += str(random.randint(0,100)) + '\n'
    filename = f'{HOME}{i}.txt'
    with open(filename, 'wt') as file:
        file.write(data)
        file.close()