
def LineAnalysis(line):
    count_star = 0
    for char in line:
        if char == '*':
            count_star += 1
        elif char == '.':
            break
    template = '*' * count_star
    line = line.removeprefix(template)
    line = line.removesuffix(template)
    line_set = set(line.split(template))
    if len(line_set) == 1 and '*' not in list(line_set)[0]:
        return True
    else:
        return False
