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
    walkers = 0
    citizens = 0
    for i in range(len(numbers) - 1):
        if numbers[i] + numbers[i+1] == 10:
            citizens +=1
            if find_symbol(text[i+1], '=') == 3:
                walkers += 1
    if citizens == walkers and citizens > 0:
        return True
    else:
        return False