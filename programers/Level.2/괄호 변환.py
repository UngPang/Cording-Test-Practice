def collect(u):
    cnt = 0
    for i in u:
        if i == '(':
            cnt += 1
        elif i == ')':
            if cnt :
                cnt -= 1
            else:
                return False
    return True

def solution(p): 
    answer = ''
    if collect(p):
        answer = p
    l, r= 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            l += 1
        elif p[i] == ')':
            r += 1
        if l == r:
            u, v = p[:i+1], p[i+1:] #2
            break

    if v:
        v = solution(v) #3

    if not collect(u): #4
        new = '(' + v + ')' #4-1,4-2,4-3
        for i in u[1:-1]: #4-4
            if i == '(':
                new += ')'
            elif i == ')':
                new += '('
        answer = new #4-5
    else:
        answer = u + v #3-1

    return answer