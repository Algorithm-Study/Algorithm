ans = [0]


def zzz(N, r, c):
    if N == 0:
        return
    na = 1 << (N-1)
    if r//na == 0 and c//na == 0:
        zzz(N - 1, r % na, c % na)
    elif r//na == 0 and c//na == 1:
        ans[0] += na * na
        zzz(N - 1, r % na, c % na)
    elif r//na == 1 and c//na == 0:
        ans[0] += na * na * 2
        zzz(N - 1, r % na, c % na)
    else:
        ans[0] += na * na * 3
        zzz(N - 1, r % na, c % na)


N, r, c = map(int, input().split())
zzz(N, r, c)
print(ans[0])