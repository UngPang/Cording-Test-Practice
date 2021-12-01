N,M = map(int, input().split())
result = []
chk = [False] * (N+1) # index를 -1 없이 바로 접근

def recur(num) :
    if num == M :
        print(' '.join(map(str, result)))
        return
    for i in range(1,N+1) :
        if chk[i] == False and (len(result)==0 or result[-1]<=i):
            result.append(i)
            recur(num+1)
            result.pop()
recur(0)
