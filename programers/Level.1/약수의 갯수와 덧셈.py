def solution(left, right):
    answer = 0
    lst=[i for i in range(left,right+1)]
    for j in lst:
        if j**0.5 == int(j**0.5):
            answer = answer - j
        else :
            answer = answer + j
    return answer