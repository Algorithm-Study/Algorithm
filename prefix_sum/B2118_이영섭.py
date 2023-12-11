N = int(input())
num = [int(input()) for _ in range(N)]
st, sv = sum(num) // 2, 0
ans = 0
li, ri = 0, 0
while li < N and ri < N:
    sv += num[ri]
    while sv > st:
        sv -= num[li]
        li += 1
    if ans < sv:
        ans = sv
    ri += 1
print(ans)
