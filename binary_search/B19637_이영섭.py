import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = []
for _ in range(N):
    ch, num = input().split()
    name.append([int(num), ch])
for _ in range(M):
    nb = int(input())
    low = 0
    high = len(name) - 1
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if name[mid][0] >= nb:
            high = mid - 1
            res = mid
        else:
            low = mid + 1
    print(name[res][1])