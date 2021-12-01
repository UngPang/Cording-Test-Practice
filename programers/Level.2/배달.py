import math
from collections import deque
def BFS(start, maps, distance, K) :
    queue = deque()
    queue.append(start)
    distance[start] = 0 # 처음 출발하는 마을의 거리는 0
    
    while queue :
        y = queue.popleft()
        for x in range(1,len(maps)) :
            if maps[y][x] != 0 : # 도착 가능한 도시인 경우
                if distance[x] > distance[y] + maps[y][x] and K >= distance[y] + maps[y][x] : 
                # 현재까지의 거리 + 이동할 때 걸리는 거리의 합이, 해당 마을까지의 거리보다 작고, K보다도 작다
                    distance[x] = distance[y] + maps[y][x]
                    queue.append(x)
    # distance 값 중 K보다 작은 값의 개수만 리턴
    return len([i for i in distance if i <= K])
                    
def solution(N, road, K):
    distance = [math.inf for j in range(N+1) ]
    # 초기마을 1에서 해당 마을까지의 거리 
    # 초기값 inf로 설정하고, 계산한 거리가 distance[마을]보다 작으면 distance 업데이트
    
    # 마을 그래프 그리기
    maps = [[0 for j in range(N+1)] for j in range(N+1)]
    for frm,to,w in road :
        # 0 일 경우 초기화한 값 그대로이므로 w 값을 넣어준다
        if maps[frm][to] == 0 and maps[to][frm] == 0 :
            maps[frm][to] = w
            maps[to][frm] = w
        else :
            # 중복된 값이 있을경우 가장 작은 w 값 사용
            if w < maps[frm][to] :
                maps[frm][to] = w
                maps[to][frm] = w
    return BFS(1, maps, distance, K)

