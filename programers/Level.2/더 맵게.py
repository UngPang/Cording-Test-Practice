import heapq
def solution(sco, k):
    answer = 0
    heapq.heapify(sco)
    while sco[0] < k :
        if len(sco) == 1 :
            answer = -1
            break
        else :
            sco1 = heapq.heappop(sco)
            sco2 = heapq.heappop(sco)
            heapq.heappush(sco, sco1 + sco2 * 2)
            answer += 1     
    return answer