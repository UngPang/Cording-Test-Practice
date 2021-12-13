from collections import deque

def solution(begin, target, words):
    queue = deque()
    chk = [0 for _ in range(len(words))]

    answer = 0
    level = 0

    # words에서 begin과 알파벳 한 개만 다른 단어를 큐에 넣는다.
    def CompareWords(word):

        # words의 모든 단어 체크 
        for i in range(len(words)):

            # 방문한 적 있는 단어는 확인하지 않는다.
            if chk[i]: continue
            
            dif = 0

            # 단어를 알파벳 단위로 체크
            for j in range(len(words[i])):
                if word[j] == words[i][j]: continue

                dif += 1

            # 알파벳이 한 개만 다른 단어만 큐에 넣는다.
            if dif != 1: continue
            
            queue.append((i, level + 1))
            chk[i] = 1
    
    CompareWords(begin)

    while queue:
        index, level = queue.popleft()
        CurrentWord = words[index]
        
        if CurrentWord == target: answer = level 

        # 현재 단어와 words를 비교한다.
        CompareWords(CurrentWord)
        
    return answer
