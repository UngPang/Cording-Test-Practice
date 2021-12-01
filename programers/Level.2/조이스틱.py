def solution(s):
    s = list(s)
    base = ["A"]*len(s)

    move_sum = 0
    shift_sum = 0
    idx = 0

    while True :
        move_right = 1
        move_left = 1

        Up_s = ord(s[idx]) - ord("A")
        Down_s = abs(ord(s[idx]) - ord("Z") - 1)
        shift_sum += min(Up_s, Down_s)
        s[idx] = "A" # To check the counted characters(shift)

        if s == base:
            break 

        for i in range(1, len(s)) :
            if s[idx+i] == "A" :
                move_right +=1
            else :
                break
            if s[idx-i] == "A" :
                move_left +=1
            else :
                break

        if move_left >= move_right :
            move_sum += move_right
            idx += move_right
        else :
            move_sum += move_left
            idx -= move_left
            
    return move_sum + shift_sum
