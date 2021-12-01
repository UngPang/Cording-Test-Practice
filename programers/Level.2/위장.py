import collections

def solution(clothes):
    answer=1
    collect = collections.defaultdict(int)
    # Counter 대신 defaultdict을 사용하면
    # 문자열 yellow_hat이 아닌, 숫자 +1 로 처리하여 효율을 높임

    for row in clothes:
        collect[row[1]]+=1
    # row[1]인 headgear,eyewear 등에 해당하는것의 개수를 셈

    for val in collect.values():
        answer*=(val+1)
    # 입지않은것을 포함하므로 +1 하여 조합개수를 구함

    return answer-1
    # 아무것도 입지않은것 -1 해줌
