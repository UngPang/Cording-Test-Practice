#﻿배열을 만들고 토너먼트를 돌리고 그 결과 배열을 만들어서 다시 토너먼트 돌리고...
def solution(n,a,b):
    answer = 0
    arr=[]
    for i in range(n) :
        arr.append(i+1)
    while True :
        answer+=1
        temp=[]
        for i in range(0,len(arr),2) :
            if arr[i] in [a,b] and arr[i+1] in [a,b] : #a와 b가 만났으면 종료!
                return answer
            if arr[i] in [a,b] :
                temp.append(arr[i])
            elif  arr[i+1] in [a,b] :
                temp.append(arr[i+1])
            else :
                temp.append(arr[i])
        # print(temp)
        arr=temp

    return answer