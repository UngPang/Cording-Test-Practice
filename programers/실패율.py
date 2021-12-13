def solution(N, stages):
    answer = []
    fail = 0
    players = len(stages)
    for i in range(1,N+1):
        cnt = stages.count(i)
        if cnt == 0 :
            fail = 0
        else :
            fail = cnt/players
        answer.append([i,fail])
        players -= cnt
    print(answer)
    answer = sorted(answer, reverse=True, key = lambda x:(x[1],-x[0]))
    answer = [j[0] for j in answer]
    return answer