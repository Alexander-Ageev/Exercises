def counter (s):
    counts = []
    for i in set(s):
        counts.append(s.count(i))
    return counts

# function separates duplicate characters from exclusion
# only works with data that has one exception
# return [duplicate, exclusion]
def separator(l):
    result = []
    if len(l) == 2:
        result = l
        return result

    if l[0] == l[1]:
        result.append(l[0])
        result.append(l[-1])
    else:
        result.append(l[1])
        result.append(l[0])
    return result

def SherlockValidString(s):
    num_diff_symbols = sorted(counter(s)) # list of different char counts
    if len(set(num_diff_symbols)) <= 2:
        sequence_info = separator(num_diff_symbols)# [base_seq, exclusion]
        if len(set(num_diff_symbols)) == 1:# string [n, n, ... , n] type ('abc')
            result = True
        elif min(counter(num_diff_symbols)) == 1 and sequence_info[1] - sequence_info[0] == 1:# string [1, n, n, ... , n] type ('abbccdd')
            result = True
        elif min(counter(num_diff_symbols)) == 1 and sequence_info[1] == 1:# string [n, n, ... , n, n+1] type ('abcdd')
            result = True
        else:
            result = False    
    else:
        result = False
    return result