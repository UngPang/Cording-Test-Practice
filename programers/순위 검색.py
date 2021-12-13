from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    # info를 파싱한다 딕셔너리에!
    db = {}
    for i in info:
        tokens = i.split(" ")
        cond = tokens[0:4]
        score = int(tokens[4])
        keys = []
        for i in range(5):
            for combi in combinations(cond, i):
                key = ('').join(list(combi))
                db.setdefault(key, []).append(score)
       
    for key in db.keys():
        db[key].sort()
    
    # query를 파싱한다!
    for q in query:
        q = q.split(" ")
        qq = ('').join([s for s in q[0:7] if s != "-" and s !="and"])
        score = int(q[7])
        if qq not in db.keys():
            answer.append(0)
        else:
            result = db[qq]
            index = bisect_left(result, score)
            answer.append(len(result) - index)

    return answer

