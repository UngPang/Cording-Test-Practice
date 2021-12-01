def solution(lottos, win_nums):
    collect = 0
    zero = lottos.count(0)
    for i in win_nums:
        if i in lottos:
            collect += 1
    maxrank = 7 - collect - zero
    minrank = 7 - collect
    if maxrank == 7:
        maxrank = 6
    if minrank == 7:
        minrank = 6       
    answer = [maxrank,minrank]
    return answer