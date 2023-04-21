x, n = map(int, input().split())
visitor = list(map(int, input().split()))
max_visit = sum(visitor[0:n])
current = max_visit
repeat = 1
for i in range(1,x-n+1):
    current = current - visitor[i-1] + visitor[i+n-1]
    if max_visit == current :
        repeat += 1
    elif max_visit < current:
        max_visit = current
        repeat = 1
if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(repeat)