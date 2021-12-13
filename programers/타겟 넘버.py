def solution(numbers, target):
    answer = 0
    def operator(i=0):
        if i < len(numbers):
            operator(i+1)
            numbers[i] *= -1
            operator(i+1)
        elif sum(numbers) == target :
            nonlocal answer
            answer += 1
    operator()       
    return answer

# 1 2 3
#     o1
#         o2
#             1 2 -3
#         1 -2 3
#         o2
#             1 -2 -3
#     -1 2 3
#     o1
#         o2
#             -1 2 -3
#         -1 -2 3
#         o2
#             -1 -2 -3
