def solution(s):
    answer = []
    s = s.replace("{", "")
    s = s.replace("}", "")
    lst = s.split(",")
    dic = {}
    
    for num in lst:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    answer = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return list(map(lambda x: int(x[0]), answer))
