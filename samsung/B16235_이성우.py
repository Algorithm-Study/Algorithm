import sys
from collections import deque
input = sys.stdin.readline

n, m, K = map(int, input().split())
fert = [list(map(int, input().split())) for _ in range(n)]
arr = [[5 for _ in range(n)] for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j, age = map(int, input().split())
    trees[i-1][j-1].append(age)

# 나이가 5의 배수인 나무는 주변으로 번식한다
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    for i in range(n):
        for j in range(n):
            death = 0
            for k in range(len(trees[i][j])):
                if arr[i][j] < trees[i][j][k]:
                    for _ in range(k, len(trees[i][j])):
                        death += trees[i][j].pop()//2
                    break
                else:
                    arr[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
            arr[i][j] += death

    for i in range(n):
        for j in range(n):
            for t in trees[i][j]:
                if t%5 == 0:
                    for idx in range(8):
                        ni = i + di[idx]
                        nj = j + dj[idx]
                        if 0 <= ni < n and 0 <= nj < n:
                            trees[ni][nj].appendleft(1)              
            arr[i][j] += fert[i][j]


answer = sum(len(trees[i][j]) for i in range(n) for j in range(n))
print(answer)