def solution(tickets):
    answer = []
    path = []   
    def DFS(start, tickets, path):
        path.append(start)
        if len(tickets) == 1: # 마지막 티켓일때
            path.append(tickets[0][1])
            answer.append(path)
            return
        else:
            # tickets 하나씩 줄이기
            for ticket in tickets:
                if ticket[0] == start:
                    copy_ticket_list=tickets.copy()
                    copy_ticket_list.remove(ticket)
                    DFS(ticket[1], copy_ticket_list, path.copy())
        
    DFS('ICN', tickets, path)  
    return min(answer) # 알파벳 순서가 앞서는 경로
