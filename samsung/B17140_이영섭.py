from collections import defaultdict

r, c, k = map(int, input().split())
board = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    tp = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = tp[j]
tm, len_row, len_col = 0, 3, 3
ans = -1

while tm <= 100:
    if board[r-1][c-1] == k:
        ans = tm
        break
    if len_row >= len_col:
        # R
        new_board = []
        max_len = 0
        for i in range(len_row):
            dd = defaultdict(int)
            for j in range(len_col):
                dd[board[i][j]] += 1
            new_list = sorted([(k, v) for k, v in dd.items() if k != 0], key=lambda x: (x[1], x[0]))
            new_list = list(sum(new_list, ()))
            if len(new_list) > 100:
                new_list = new_list[:100]
                max_len = 100
            else:
                max_len = max(max_len, len(new_list))
                new_list += [0 for _ in range(100 - len(new_list))]
            new_board.append(new_list)
        for i in range(100 - len_row):
            new_board.append([0 for _ in range(100)])
        len_col = max_len

    else:
        # C
        new_board = [[] for _ in range(100)]
        max_len = 0
        for i in range(len_col):
            dd = defaultdict(int)
            for j in range(len_row):
                dd[board[j][i]] += 1
            new_list = sorted([(k, v) for k, v in dd.items() if k != 0], key=lambda x: (x[1], x[0]))
            new_list = list(sum(new_list, ()))
            if len(new_list) > 100:
                new_list = new_list[:100]
                max_len = 100
            else:
                max_len = max(max_len, len(new_list))
                new_list += [0 for _ in range(100 - len(new_list))]
            for j in range(100):
                new_board[j].append(new_list[j])
        for i in range(100):
            new_board[i] += [0 for _ in range(100 - len(new_board[i]))]
        len_row = max_len
    board = new_board
    tm += 1
print(ans)
