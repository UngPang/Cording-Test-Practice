import math
def solution(pro, spd):
    answer = []
    cnt = 0
    day = 0
    while len(pro) > 0 :
        if pro[0]+spd[0]*day >= 100 :
            pro.pop(0)
            spd.pop(0)
            cnt += 1
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            day += 1            
    answer.append(cnt)
    return answer