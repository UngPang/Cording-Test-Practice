def solution(n, lost, reserve):
    a_reserve = set(reserve)-set(lost)
    a_lost = set(lost)-set(reserve)
    for i in a_reserve :
        if i-1 in a_lost :
            a_lost.remove(i-1)
        elif i+1 in a_lost :
            a_lost.remove(i+1)
    return n-len(a_lost)