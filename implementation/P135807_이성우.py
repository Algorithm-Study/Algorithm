import math
def solution(arrayA, arrayB):
    x = 0
    y = 0
    # 0, n의 최대공약수는 n이다
    for idx in range(len(arrayA)):
        x = math.gcd(x,arrayA[idx])
        y = math.gcd(y,arrayB[idx])

    for idx in range(len(arrayA)):
        if arrayA[idx] % y == 0:
            y = 1
        if arrayB[idx] % x == 0:
            x = 1
    # print(x,y)
    if x == 1 and y ==1:
        return 0
    else:
        return max(x,y)