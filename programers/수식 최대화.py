import re
from itertools import permutations

def solution(expression):
    answer = 0
    # 숫자, 연산자 분리
    num = re.split('\+|\-|\*', expression)
    opr = re.split('[0-9]+', expression)[1:-1]
    for order in permutations("+-*", 3):
        nc = num.copy()
        oc = opr.copy()
        for o in order:
            idx = 0
            while idx < len(oc):
                if oc[idx] == o:
                    nc[idx] = str(eval(''.join((nc[idx], o, nc[idx + 1]))))
                    # eval : str형태 수식을 계산해준다
                    nc.pop(idx + 1)
                    oc.pop(idx)
                    idx -= 1
                idx += 1
        answer = max(answer, abs(int(nc[0])))
    return answer

