from fractions import Fraction
n = int(input())**2
u1, u2 = 0, -9999999
count = 0
while True:
    v1 = Fraction((1-n), (1+n))*u1 + Fraction((2*n), (1+n))*u2
    v2 = Fraction(2, (1+n))*u1 - Fraction((1-n), (1+n))*u2
    count += 1
    u1, u2 = v1, v2
    # 벽에 부딪친 경우
    if u1 <= 0:
        if u1 < 0:
            count += 1
        u1 = -u1
    # 거리가 좁혀질 수 없는 경우
    if (u2-u1) >= 0:
        break
print(count)