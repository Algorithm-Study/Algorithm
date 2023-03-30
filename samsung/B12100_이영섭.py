import sys
input = sys.stdin.readline

def permutations(arr, r, prefix):
    for i in range(len(arr)):
        if arr[i] in prefix: continue
        if r == 1: yield [arr[i]]
        else:
            prefix.append(i)
            for next in permutations(arr, r-1, prefix):
                yield [arr[i]] + next
            prefix.pop()

def mv_board(board, st, ed, rep, ed2, ver):
    if ver == True:
        for i in range(N):
            temp = []
            cont = False
            for j in range(st, ed, rep):
                print(i, j, board[j][i])
                if board[j][i] == 0:
                    print(0)
                    continue
                else:
                    if board[j][i] == board[j+rep][i] and cont == False:
                        cont = True
                        temp.append(board[j][i] + board[j+rep][i])
                        print(1, j, i, temp)
                    elif board[j][i] != board[j+rep][i] and cont == False:
                        cont = False
                        temp.append(board[j][i])
                        print(2, j, i, temp)
                    else: 
                        cont = False
                        print(3)
                        continue
            if cont == False:
                temp.append(board[ed][i])
            print(temp)
            for j, k in zip(range(N), range(st, ed2, rep)):
                if j < len(temp):
                    board[k][i] = temp[j]
                else:
                    board[k][i] = 0
    else:
        for i in range(N):
            temp = []
            cont = False
            for j in range(st, ed, rep):
                if board[i][j] == 0:
                    continue
                else:
                    if board[i][j] == board[i][j+rep] and cont == False:
                        cont = True
                        temp.append(board[i][j] + board[i][j+rep])
                    elif board[i][j] != board[i][j+rep] and cont == False:
                        cont = False
                        temp.append(board[i][j])
                    else: 
                        cont = False
                        continue
            if cont == False:
                temp.append(board[i][ed])
            # print(temp)
            for j, k in zip(range(N), range(st, ed2, rep)):
                # print(j, k)
                if j < len(temp):
                    board[i][k] = temp[j]
                    # print(-1, board[i][k], temp[j])
                else:
                    board[i][k] = 0
                    # print(-2, board[i][k])

def move(new_board, dir):
    print(new_board)
    if dir == 'U':
        mv_board(new_board, 0, N-1, 1, N, True)
    elif dir == 'L':
        mv_board(new_board, 0, N-1, 1, N, False)
    elif dir == 'D':
        mv_board(new_board, N-1, 0, -1, -1, True)
    else:
        mv_board(new_board, N-1, 0, -1, -1, False)
    print(new_board)
    return new_board

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dm = ['U', 'D', 'L', 'R']
# bf = list(permutations(dm, 5, []))
bf = ['L', 'U', 'L', 'D', 'L']
result = 0
for case in bf:
    new_board = [row[:] for row in board]
    for mv in case:
        new_board = move(new_board, mv)
        max_val = max(map(max, new_board))
        if max_val > result:
            result = max_val
print(result)