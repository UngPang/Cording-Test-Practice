def queen(n):
    global count
    if len(n) == N:
        count += 1
    else:
        for x in range(N):
            if x in n:
                continue
            for i in range(len(n)):
                if abs(x - n[i]) == len(n) - i: # 대각선 배치가 됐는지 아닌지
                    break
            else: # 모든 퀸이 대각선 배치가 되지 않았을 때
                n.append(x)
                queen(n)
                n.pop()

N = int(input())
count = 0

for i in range(N):
    queen([i])

print(count)
# python3 로는 시간초과가 나고 pypy3로 정답처리됌 개선해야함