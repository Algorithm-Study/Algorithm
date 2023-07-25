r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

def operation(arr, l):
    for idx, row in enumerate(arr):
        temp = []
        for n in set(row):
            if n:
                temp.append((n, row.count(n)))
        temp = sorted(temp, key = lambda x : (x[1], x[0]))
        templen = len(temp)
        if templen > 50 : templen = 50
        l = max(l, templen * 2)
        arr[idx] = []
        for i in range(templen):
            arr[idx].append(temp[i][0])
            arr[idx].append(temp[i][1])
    
    for idx, row in enumerate(arr):
        for _ in range(l-len(row)):
            arr[idx].append(0)
    
    return arr, l

row, col = 3, 3
for t in range(101):
    if r <= row and c <= col and arr[r-1][c-1] == k:
        print(t)
        break
    
    if row >= col:
        arr, col = operation(arr, col)
    else:
        arr, row = operation(list(zip(*arr)), row)
        arr = list(zip(*arr))
else:
    print(-1)
        