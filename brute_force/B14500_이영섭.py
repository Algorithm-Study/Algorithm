from itertools import combinations
import sys
input = sys.stdin.readline

square = [[0, 1], [1, 0], [1, 1]]
long_hor = [[0, 1], [0, 2], [0, 3]]
long_ver = [[1, 0], [2, 0], [3, 0]]
hexa_hor = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]
hexa_ver = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]]
idx = [0, 1, 2, 3, 4, 5]
bf = list(combinations(idx, 4))
not_in_hor = [(0, 2, 3, 5), (0, 1, 3, 5), (0, 2, 3, 4), (0, 2, 4, 5), (1, 2, 3, 5), (0, 1, 3, 4), (1, 2, 4, 5)]
not_in_ver = [(0, 1, 4, 5), (0, 3, 4, 5), (1, 2, 4, 5), (0, 1, 2, 5), (0, 1, 3, 4), (0, 1, 2, 3), (2, 3, 4, 5)]
bf_hor = [i for i in bf if i not in not_in_hor]
bf_ver = [i for i in bf if i not in not_in_ver]
max_val = 0
N, M = map(int, input().rstrip().split())
paper = []
for i in range(N):
    temp = list(map(int, input().rstrip().split()))
    paper.append(temp)

# square
for i in range(N-1):
    for j in range(M-1):
        val = paper[i][j]
        for k in square:
            val += paper[i+k[0]][j+k[1]]
        if val > max_val:
            max_val = val
            
# long_hor
for i in range(N):
    for j in range(M-3):
        val = paper[i][j]
        for k in long_hor:
            val += paper[i+k[0]][j+k[1]]
        if val > max_val:
            max_val = val
            
# long_ver
for i in range(N-3):
    for j in range(M):
        val = paper[i][j]
        for k in long_ver:
            val += paper[i+k[0]][j+k[1]]
        if val > max_val:
            max_val = val
            
# hexa_hor
for i in range(N-2):
    for j in range(M-3):
        for k in bf_hor:
            val = 0
            for l in k:
                val += paper[i+hexa_hor[l][0]][j+hexa_hor[l][1]]
            if val > max_val:
                max_val = val
            
# hexa_ver
for i in range(N-3):
    for j in range(M-2):
        for k in bf_ver:
            val = 0
            for l in k:
                val += paper[i+hexa_ver[l][0]][j+hexa_ver[l][1]]
            if val > max_val:
                max_val = val
            
print(max_val)