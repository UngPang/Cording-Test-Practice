def solution(s):
    answer = 1000
    if len(s)==1:
        answer = 1
    for i in range(1, int(len(s)/2)+1):
        compressLen = 0
        prev = s[0:i]
        count = 1
        
        for j in range(i, len(s), i):
            if(j+i > len(s)):
                compressLen += (len(s)-j)
                break
            
            curr = s[j:j+i]

            if(prev == curr):
                count += 1
            else:
                prev = curr
                if(count < 2):
                    compressLen += i
                else:
                    compressLen += len(str(count))+i
                count = 1

        if(count < 2):
            compressLen += i
        else:
            compressLen += len(str(count))+i
        if(answer > compressLen):
            answer = compressLen

    return answer