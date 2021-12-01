from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course: # 2
        lst = []
        for o in orders: # ABCFG 
            com = combinations(sorted(o), c) # AB AC AF AG BC BF...
            lst += com
        cnt = Counter(lst) 
        print(cnt)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            answer += [''.join(f) for f in cnt if cnt[f] == max(cnt.values())]
    return sorted(answer)