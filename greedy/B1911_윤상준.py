n, l = map(int, input().split())
pools = []
for _ in range(n):
    pools.append(tuple(map(int, input().split())))
pools.sort()
count = 0
prev_end = pools[0][0]
for i in range(n):
    start,end = pools[i]
    if start <= prev_end:
        start = prev_end
    if (end-start) % l:
        prev_end = end + l- (end-start) % l
        count += 1
    count += (end-start) // l
print(count)      