def solution(nums):
    prime = 0
    sums = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sums = nums[i] + nums[j] + nums[k]
                for a in range(2,sums) :
                    if sums % a == 0 :
                        break
                else :
                    prime += 1
    return prime
