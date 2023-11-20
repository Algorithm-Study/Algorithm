import math

N, L = map(int, input().split())
pond = []
for _ in range(N):
    st, ed = map(int, input().split())
    pond.append((st, ed))
pond.sort()

ans = 0
loc = 0
for ps, pe in pond:
    ps = max(ps, loc)
    cnt = math.ceil((pe - ps) / L)
    loc = ps + cnt * L
    ans += cnt

print(ans)