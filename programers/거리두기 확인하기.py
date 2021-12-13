# 상하좌우 움직일 배열
x=[0,1,0,-1]
y=[1,0,-1,0]
# 한 명 P만을 기점으로 bfs 진행
def bfs(i,j,place,visit):
    # P위치 i,j로 시작
    queue=[(i,j)]
    visit[i][j]=1
    while queue:
        top_y,top_x=queue.pop(0)
        for k in range(4):
            newx=top_x+x[k]
            newy=top_y+y[k]
            # 5x5배열을 벗어나지 않으며 방문하지 않았고 맨해튼 거리 만족하면서 빈칸이 아닐 때를 찾기 위함
            if newx<0 or newx>4 or newy<0 or newy>4 or visit[newy][newx]==1 or (abs(i-newy)+abs(j-newx))>2 or place[newy][newx]=='X':
                continue
            # 맨해튼 거리 내에서 다른 사람을 발견할 경우, 방역수칙 위반
            if place[newy][newx]=='P':
                return 0
            visit[newy][newx]=1
            queue.append((newy,newx))
    # 무사히 통과했다면 이 사람은 방역수칙을 준수하였음
    return 1

# 하나의 강의실을 기준으로 검사
def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                visit=[[0]*5 for i in range(5)]
                if bfs(i,j,place,visit)==0:
                    return 0
    return 1
    
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer