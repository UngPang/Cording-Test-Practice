def gcd(x,y):
    if y == 0 :
        return x
    else :
        return gcd(y,x%y)
def solution(w,h):
    square = [w,h]
    square.sort()
    a = gcd(square[1],square[0])
    answer = w*h - (w/a + h/a - 1)*a
    return answer