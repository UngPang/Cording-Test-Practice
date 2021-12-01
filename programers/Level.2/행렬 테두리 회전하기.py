def solution(rows, columns, queries):
    answer = []
    result = []
    for i in range(rows) :
        answer.append(list(range(1+i*columns,1+columns+i*columns))) # [[1,2,3,4,5,6],[7,8,9,10,11,12],...]
    for k in queries : # [2,2,5,4]
        lst = []
        for i in range(k[1]-1,k[3]): # 1 2 3
            lst.append(answer[k[0]-1][i]) # 8 9 10
        for i in range(k[0],k[2]): # 2 3 4
            lst.append(answer[i][k[3]-1]) # 16 22 28
        for i in range(k[3]-2,k[1]-2,-1): # 2 1 
            lst.append(answer[k[2]-1][i]) # 27 26 
        for i in range(k[2]-2,k[0]-1,-1): # 3 2
            lst.append(answer[i][k[1]-1]) # 20 14
        new = []
        new = lst[:-1]
        new.insert(0,lst[-1]) # new = 14 8 9 10 16 22 28 27 26 20 / lst = 8 9 10 16 22 28 27 26 20 14
        cnt = 0
        for i in range(k[1]-1,k[3]): # 1 2 3 
            answer[k[0]-1][i] = new[cnt] # 8 -> 14 , 9 -> 8, 10 -> 9
            cnt += 1
        for i in range(k[0],k[2]): # 2 3 4
            answer[i][k[3]-1] = new[cnt] # 16 -> 10, 22 -> 16, 28 -> 22
            cnt += 1
        for i in range(k[3]-2,k[1]-2,-1): # 2 1
            answer[k[2]-1][i] = new[cnt] # 27 -> 28, 26 -> 27
            cnt += 1
        for i in range(k[2]-2,k[0]-1,-1): # 3 2
            answer[i][k[1]-1] = new[cnt] # 20 -> 26, 14 -> 20
            cnt += 1
        result.append(min(lst))    
    return result        