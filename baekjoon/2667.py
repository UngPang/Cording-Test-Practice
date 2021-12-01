N = int(input())
map = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x) :
    global each
    each += 1
    for k in range(4) :
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < N :
            if map[ny][nx] == 1 and chk[ny][nx] == False :
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N) :
    for i in range(N) :
        if map[j][i] == 1 and chk[j][i] == False :
            # 방문 체크 표시
            chk[j][i] = True
            # 전역변수로 각각의 계산 표현 계산마다 0으로 초기화
            each = 0
            # DFS로 크기 구하기
            dfs(j,i)
            # 크기를 결과값리스트에 포함
            result.append(each)


result.sort()
print(len(result))
for i in result :
    print(i)