t = int(input())

for i in range(t):
    n=int(input())
    zero = [1,0]
    one = [0,1]
    for j in range(2,n+1):
        cnt_0 = zero[j-1] + zero[j-2]
        zero.append(cnt_0)
        cnt_1 = one[j-1] + one[j-2]
        one.append(cnt_1)
    
    print(zero[n], one[n])

