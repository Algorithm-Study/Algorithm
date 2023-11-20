n, l = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key= lambda x: (x[0], x[1]))
board = arr[0][0]
cnt = 0
for start, end in arr:
    if board > end:
        continue
    elif board < start:
        board = start
    dist = end - board
    r = 1
    if dist%l == 0:
        r = 0
    count = dist//l + r
    board += count*l
    cnt += count
print(cnt)