def split_string(s):
    text = []
    numbers = []
    temp_str = ''
    for char in s:
        if char.isdigit():
            numbers.append(int(char))
            text.append(temp_str)
            temp_str = ''
        else:
            temp_str += char
    text.append(temp_str)
    return [text, numbers]

def find_symbol(s, sym):
    count = 0
    while sym in s:
        count += 1
        s = s[s.find(sym)+1:]
    return count

def white_walkers(village):
    temp = split_string(village)
    numbers = temp[1]
    text = temp[0]
    num_walkers = 0
    num_citizens = 0
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i+1] == 10:
            num_citizens +=1
            if find_symbol(text[i+1], '=') == 3:
                num_walkers += 1
    if num_citizens == num_walkers and num_citizens > 0:
        walkers_found = True
    else:
        walkers_found = False
    return walkers_found