import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input().rstrip())
arr = [list(input().rstrip()) for _ in range(m)]
dict_ = {}
for i in range(n+1):
    dict_[(0, i)] = [0, 0, 0]
for i in range(m+1):
    dict_[(i, 0)] = [0, 0, 0]
idx = ['J', 'O', 'I']

for r in range(1, m+1):
    for c in range(1, n+1):
        tmp = [0, 0, 0]
        tmp[idx.index(arr[r-1][c-1])] += 1
        for i in range(3):
            tmp[i] += dict_[(r, c-1)][i] 
            tmp[i] += dict_[(r-1, c)][i]
            tmp[i] -= dict_[(r-1, c-1)][i]
        dict_[(r, c)] = tmp

for _ in range(k):
    answer = [0, 0, 0]
    a, b, c, d = map(int, input().split())
    for i in range(3):
        answer[i] += dict_[(c, d)][i]
        answer[i] -= dict_[(c, b-1)][i]
        answer[i] -= dict_[(a-1, d)][i]
        answer[i] += dict_[(a-1, b-1)][i]
    print(*answer)