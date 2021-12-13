def solution(record):
    answer = []
    temp = []
    name = {}
    for i in record:
        log = i.split()
        if log[0] != 'Leave': name[log[1]] = log[2]
        if log[0] != 'Change': temp.append((log[0], log[1]))

    for action, id in temp:
        msg = "님이 들어왔습니다." if action == "Enter" else "님이 나갔습니다."
        answer.append(name[id] + msg)
    
    return answer