n, m = map(int, input().split())
holes = list(map(int, input().split()))
prefix = [0]*(n+1)
for _ in range(m):
    a,b,depth = map(int, input().split())
    prefix[a-1] += depth
    prefix[b] -= depth
count = 0
for i in range(n):
    count += prefix[i]
    print(holes[i] + count, end = ' ')