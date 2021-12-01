n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]


dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x) :
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m :
                if map[ny][nx] == 1 and chk[ny][nx] == False :
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n) :
    for i in range(m) :
        if map[j][i] == 1 and chk[j][i] == False :
        # 값이 1이고 방문하지 않은 경우 
            chk[j][i] = True
            cnt += 1
            # 전체 그림 갯수 +1
            maxv = max(maxv, bfs(j,i))
            # 최댓값 갱신

print(cnt)
print(maxv)