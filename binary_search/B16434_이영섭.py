N, A = map(int, input().split())
arr = []
for _ in range(N):
    t, a, h = map(int, input().split())
    arr.append((t, a, h))


def can_clear(atk, maxhp):
    curhp = maxhp
    for t, a, h in arr:
        if t == 1:
            turn = h // atk if not h % atk else h // atk + 1
            curhp -= a * (turn - 1)
        else:
            atk += a
            curhp += h
            if curhp > maxhp:
                curhp = maxhp
        if curhp <= 0:
            return False
    return True


ans = 0
st, ed = 1, N * int(1e6) * int(1e6)
while st <= ed:
    mid = (st + ed) // 2
    if can_clear(A, mid):
        ed = mid - 1
        ans = mid
    else:
        st = mid + 1
print(ans)
