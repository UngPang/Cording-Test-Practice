from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
a, b, c, d = list(map(int, input().split()))

min_answer = int(1e9)
max_answer = -int(1e9)
answer = 0
def dfs(i, now):
    global answer, min_answer,max_answer,  a, b, c, d
    if i == n:
        min_answer = min(min_answer, now)
        max_answer = max(max_answer, now)
    else:
        if a>0:
            a-=1
            dfs(i + 1, now + num_list[i])
            a+=1
        if b>0:
            b-=1
            dfs(i + 1, now - num_list[i])
            b+=1
        if c>0:
            c-=1
            dfs(i+1, now * num_list[i])
            c+=1
        if d>0:
            d-=1
            if now <0 :
                dfs(i + 1, -((-now) // num_list[i]))
            else:
                dfs(i + 1, now // num_list[i])
            d+=1

dfs(1, num_list[0])
print(max_answer)
print(min_answer)


