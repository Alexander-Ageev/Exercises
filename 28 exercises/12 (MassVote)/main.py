def MassVote(N, Votes):
    all_votes = sum(Votes)
    Votes = [float(format( (Votes[i]/all_votes) * 100, '.3f' ) )  for i in range(N)]
    num_max_votes_person = max(Votes)
    index = -1
    max_count = 0
    for i in range(N):
        if Votes[i] == num_max_votes_person:
            index = i
            max_count += 1
    if 0 <= max_count > 1:
        result = 'no winner'
    elif Votes[index] > 50:
        result = 'majority winner ' + str(index+1)
    elif Votes[index] <= 50:
        result = 'minority winner ' + str(index+1)
    return result