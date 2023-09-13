from itertools import permutations
import copy

def rotate(arr, r, c, s):
    for d in range(1, s + 1):
        tmp = arr[r - d][c - d]
        for i in range(r - d, r + d):
            arr[i][c - d] = arr[i + 1][c - d]
        for i in range(c - d, c + d):
            arr[r + d][i] = arr[r + d][i + 1]
        for i in range(r + d, r - d, -1):
            arr[i][c + d] = arr[i - 1][c + d]
        for i in range(c + d, c - d + 1, -1):
            arr[r - d][i] = arr[r - d][i - 1]
        arr[r - d][c - d + 1] = tmp

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(k)]

answer = float('inf')

for cases in permutations(commands, k):
    tmp = copy.deepcopy(arr)
    for command in cases:
        r, c, s = command
        rotate(tmp, r - 1, c - 1, s)
    for row in tmp:
        answer = min(answer, sum(row))

print(answer)