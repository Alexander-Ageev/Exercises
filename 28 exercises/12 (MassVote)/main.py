MAJORITY_LIMIT = 50

def MassVote(N, Votes):
    all_votes = sum(Votes)
    if not (all_votes == 0):
        Votes = [float(format( (Votes[i]/all_votes) * 100, '.3f' ) )  for i in range(N)]
        max_vote_index = -1
        leaders_count = 0
        for person in range(N):
            if Votes[person] == max(Votes):
                max_vote_index = person
                leaders_count += 1
        if leaders_count != 1:
            winner = 'no winner'
        elif Votes[max_vote_index] > MAJORITY_LIMIT:
            winner = 'majority winner ' + str(max_vote_index+1)
        elif Votes[max_vote_index] <= MAJORITY_LIMIT:
            winner = 'minority winner ' + str(max_vote_index+1)
    return winner