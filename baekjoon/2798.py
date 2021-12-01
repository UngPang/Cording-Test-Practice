N, M = map(int, input().split())
card = list(map(int, input().split()))
result = 0

for i in card:
    for j in card:
        if i == j:
            continue
        for k in card:
            if k == i or k == j:
                continue
            sum = i + j + k
            if sum > M:
                continue
            elif sum > result:
                result = sum

print(result)