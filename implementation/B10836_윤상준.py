import sys
input = sys.stdin.readline
n, m = map(int, input().split())
bugs = [[1]*n for _ in range(n)]
info = [0]*(2*n-1)
for _ in range(m):
    zero,one,two = map(int, input().split())
    for i in range(zero, zero + one):
        info[i] += 1
    for i in range(zero + one, 2 * n - 1):
        info[i] += 2
idx = 0
for i in range(n-1,-1,-1):
    bugs[i][0] += info[idx]
    idx += 1
for i in range(1,n):
    bugs[0][i] += info[idx]
    idx += 1
for i in range(1,n):
    for j in range(1,n):
        bugs[i][j] += bugs[0][j]-1
for i in range(n):
    print(*bugs[i])
# 전체 일수 동안 각 애벌레의 성장 크기를 구하기
# 이후 최종 크기를 구하면 문제 해결