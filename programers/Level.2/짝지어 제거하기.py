def solution(s):
    answer = 1
    lst =[]
    for i in s :
        if lst and i == lst[-1] :
            del lst[-1]
        else :
            lst.append(i)
    if lst :
        answer = 0
    return answer