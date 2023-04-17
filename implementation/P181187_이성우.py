import math
def solution(r1, r2):
    cnt = 0
    def y(r,x):
        return (r**2 - x**2)**0.5
    for i in range(1, r2+1):
        y2 = y(r2,i)
        if r1 <= i:
            y1 = 0
        else:
            y1 = y(r1,i)
        cnt += int(y2) - math.ceil(y1) +1

    return (cnt*4) 
