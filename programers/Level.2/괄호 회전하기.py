from collections import deque
def solution(s):
    def check():
        stack = []
        for c in li:
            if c in ('[', '(', '{'):
                stack.append(c)
            else:
                if not stack: return False
                x = stack.pop()
                if c == ']' and x != '[':
                    return False
                elif c == ')' and x != '(':
                    return False
                elif c == '}' and x != '{':
                    return False
        if stack: 
            return False
        return True

    answer = 0
    for i in range(len(s)):
        li = deque(s)
        li.rotate(-i)
        if check(): answer += 1

    return answer