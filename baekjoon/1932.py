n = int(input())
t = []
for _ in range(n):
    t.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(i+1) :
        if j == 0 : # 왼쪽변인경우
            t[i][j] += t[i-1][j]
        elif j == i : # 오른쪽변인경우
            t[i][j] += t[i-1][j-1]
        else :
            t[i][j] += max(t[i-1][j],t[i-1][j-1])
print(max(t[-1]))