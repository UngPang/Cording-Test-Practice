from collections import deque
def solution(maps):
    answer = -1
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    n, m = (len(maps[0]),len(maps))
    queue = deque([(0,0,1)])
    
    while queue :
        x,y,d = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx > -1 and ny > -1 and nx < n and ny < m :
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1 :
                    maps[ny][nx] = d + 1
                    if nx == n - 1 and ny == m - 1 :
                        answer = d + 1
                    queue.append((nx,ny,d+1))
    return answer