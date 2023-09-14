import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

prefix = [[0]*(m+1) for _ in range(n+1)]

for r in range(1, n+1):
    for c in range(1, m+1):
        if (r + c) % 2 == 0:
            prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]
            if arr[r-1][c-1] == 'W':
                prefix[r][c] += 1
        else:
            prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1]
            if arr[r-1][c-1] == 'B':
                prefix[r][c] += 1

maximum = -float('inf')
minimum = float('inf')

for r in range(k, n+1):
    for c in range(k, m+1):
        maximum = max(prefix[r][c] - prefix[r-k][c] - prefix[r][c-k] + prefix[r-k][c-k], maximum)
        minimum = min(prefix[r][c] - prefix[r-k][c] - prefix[r][c-k] + prefix[r-k][c-k], minimum)

print(min(maximum, minimum, k*k - maximum, k*k - minimum))
