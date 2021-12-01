def solution(absolutes, signs):
    plus = []
    minus = []
    for i in range(len(signs)):
        if signs[i] == True :
            plus.append(absolutes[i])
        if signs[i] == False :
            minus.append(absolutes[i])
            
    answer = sum(plus) - sum(minus)
    
    return answer
