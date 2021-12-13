def solution(nums):
    answer = len(nums)/2
    core = list(set(nums))
    if len(core)<answer :
        answer = len(core)
    return answer