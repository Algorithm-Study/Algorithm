tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())

    arr.sort()
    for idx in range(n-1):
        if arr[idx+1].startswith(arr[idx]):
            print('NO')
            break
    else:
        print('YES')