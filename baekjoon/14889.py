# 모든 경우의 수를 탐색해야하므로 '백트래킹'을 이용하여 탐색한다.
# '0팀'과 '1팀'으로 분할한다.
# 각 팀에는 n//2 만큼의 플레이어가 들어간다.
# flag[x] == 0이면 '0팀'이고 flag[x] == 1이면 '1팀'이다.
# 따라서, sum(flag) == n//2 라면, 팀 분할이 완료되었다는 뜻이다.
# 팀 분할이 완료되면 minimum 값을 업데이트해주고 백트래킹 한다.

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
flag = [0 for _ in range(n)]
global mini
mini = 1000000


def backtrack(num):
    global mini
    # n//2만큼의 플레이어가 나뉘면
    if sum(flag) == n // 2:
        # '0팀'과 '1팀'의 능력치 합을 temp에 저장
        temp = [0, 0]
        for i in range(n):
            for j in range(i+1, n):
                if flag[i] == flag[j]:
                    temp[flag[i]] += s[i][j] + s[j][i]
        # 차를 계산해준 뒤, 기존 minimum보다 작으면 업데이트 해준다.
        tmp = abs(temp[0] - temp[1])
        if tmp < mini:
            mini = tmp
        return
    # 겹치지 않도록 백트래킹을 해준다.
    for i in range(num+1, n):
        flag[i] = 1
        backtrack(i)
        flag[i] = 0


backtrack(-1)
print(mini)


