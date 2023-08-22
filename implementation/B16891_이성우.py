def collision(a_v, b_v):
    a_v, b_v = \
        (a-b)*a_v/(a+b) + 2*b*b_v/(a+b), 2*a*a_v/(a+b) - (a-b)*b_v/(a+b)
    
    return a_v, b_v

a ,b = 1, int(input())**2
a_v, b_v = 0, -1
cnt = 0
while a_v > b_v:
    a_v, b_v = collision(a_v, b_v)
    cnt += 1
    if 0 > a_v:
        a_v *= -1
        cnt += 1
print(cnt)

# a_v, b_v 변경을 한 줄에 쓰지 않아서 오류가 났었다