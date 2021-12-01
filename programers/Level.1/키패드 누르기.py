def solution(numbers, hand):
    left = [1,4,7,10]
    right = [3,6,9,11]
    middle = [2,5,8,0]
    left_location = 10
    right_location = 11
    answer = ''
    for i in numbers:
        if i in left:
            answer += 'L'
            left_location = i
        elif i in right:
            answer += 'R'
            right_location = i
        else :
            if left_location in left:
                left_distance = middle.index(i) - left.index(left_location)
                if left_distance <0:
                    left_distance = left_distance*-1
                left_distance = left_distance +1
            elif left_location in middle:
                left_distance = middle.index(i) - middle.index(left_location)
                if left_distance <0:
                    left_distance = left_distance*-1
            if right_location in right:
                right_distance = middle.index(i) - right.index(right_location)
                if right_distance <0:
                    right_distance = right_distance*-1
                right_distance = right_distance +1
            elif right_location in middle:
                right_distance = middle.index(i) - middle.index(right_location)
                if right_distance <0:
                    right_distance = right_distance*-1
            if left_distance < right_distance :
                answer += 'L'
                left_location = i
            elif right_distance < left_distance :
                answer += 'R'
                right_location = i
            else:
                if hand == 'left':
                    answer +='L'
                    left_location = i
                elif hand == 'right': 
                    answer +='R'
                    right_location = i
    return answer