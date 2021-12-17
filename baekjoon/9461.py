n = int(input())
memo = {1:1,2:1,3:1,4:2,5:2}
def triangle(number:int) -> int:
    if number in memo:
        return memo[number]
    memo[number] = triangle(number-1) + triangle(number-5)
    return memo[number]
for i in range(n) :
    num = int(input())
    print(triangle(num))
