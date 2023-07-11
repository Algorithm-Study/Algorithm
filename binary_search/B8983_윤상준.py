import bisect
m,n,l = map(int,input().split())
shoots = sorted(list(map(int, input().split())))
total = 0
for _ in range(n):
    x, y = map(int, input().split())
    idx = bisect.bisect_left(shoots,x)
    for i in (idx-1,idx):
        if i < 0 or i >= m:
            continue
        if abs(shoots[i]-x) + y <= l:
            total += 1
            break
print(total)
# y축 값은 모두 사수들에게 동일
# x축 값의 거리가 중요