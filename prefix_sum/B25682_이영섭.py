n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

prefix_sum = [[0]*(m+1) for _ in range(n+1)]
prefix_other = [[0]*(m+1) for _ in range(n+1)]


def make_prefix_sum(color):
    for i in range(1, n):
        if i % 2 == 0:
            if board[i][0] == color:
                prefix_sum[i][0] = prefix_sum[i - 1][0]
            else:
                prefix_sum[i][0] = prefix_sum[i - 1][0] + 1
        else:
            if board[i][0] == color:
                prefix_sum[i][0] = prefix_sum[i - 1][0] + 1
            else:
                prefix_sum[i][0] = prefix_sum[i - 1][0]

    for i in range(1, m):
        if i % 2 == 0:
            if board[0][i] == color:
                prefix_sum[0][i] = prefix_sum[0][i - 1]
            else:
                prefix_sum[0][i] = prefix_sum[0][i - 1] + 1
        else:
            if board[0][i] == color:
                prefix_sum[0][i] = prefix_sum[0][i - 1] + 1
            else:
                prefix_sum[0][i] = prefix_sum[0][i - 1]

    for i in range(1, n):
        for j in range(1, m):
            if ((i+j) % 2 == 0 and board[i][j] == color) or ((i+j) % 2 == 1 and board[i][j] != color):
                prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]
            else:
                prefix_sum[i][j] = prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + 1

    for i in range(n):
        for j in range(m):
            prefix_other[i][j] = (i+1)*(j+1) - prefix_sum[i][j]


make_prefix_sum(board[0][0])
for i in range(n+1):
    prefix_sum[i] = [0] + prefix_sum[i]
    prefix_other[i] = [0] + prefix_other[i]
prefix_sum = [[0] * (m+2)] + prefix_sum
prefix_other = [[0] * (m+2)] + prefix_other

ans = float('inf')
other_ans = float('inf')
for i in range(n - k + 1):
    for j in range(m - k + 1):
        ans = min(ans, prefix_sum[i + k][j + k] - prefix_sum[i][j + k] - prefix_sum[i + k][j] + prefix_sum[i][j])
        other_ans = min(other_ans, prefix_other[i + k][j + k] - prefix_other[i][j + k] - prefix_other[i + k][j] + prefix_other[i][j])
print(min(ans, other_ans))
