import sys
input = sys.stdin.readline

def product(arr, r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for next in product(arr, r-1):
                yield [arr[i]] + next

def move(board, dir):
    if dir == 'U':
        for i in range(N):
            temp = []
            tmp = []
            cont = False
            for j in range(N):
                if board[j][i] != 0:
                    temp.append(board[j][i])
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1] and cont == False:
                    tmp.append(temp[j]*2)
                    cont = True
                elif temp[j] != temp[j+1] and cont == False:
                    tmp.append(temp[j])
                elif cont == True:
                    cont = False
            if cont == False and len(temp) >= 1:
                tmp.append(temp[-1])
            for j in range(N):
                if j < len(tmp):
                    board[j][i] = tmp[j]
                else:
                    board[j][i] = 0
    elif dir == 'D':
        for i in range(N):
            temp = []
            tmp = []
            cont = False
            for j in range(N-1, -1, -1):
                if board[j][i] != 0:
                    temp.append(board[j][i])
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1] and cont == False:
                    tmp.append(temp[j]*2)
                    cont = True
                elif temp[j] != temp[j+1] and cont == False:
                    tmp.append(temp[j])
                elif cont == True:
                    cont = False
            if cont == False and len(temp) >= 1:
                tmp.append(temp[-1])
            for idx, j in enumerate(range(N-1, -1, -1)):
                if idx < len(tmp):
                    board[j][i] = tmp[idx]
                else:
                    board[j][i] = 0
    elif dir == 'L':
        for i in range(N):
            temp = []
            tmp = []
            cont = False
            for j in range(N):
                if board[i][j] != 0:
                    temp.append(board[i][j])
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1] and cont == False:
                    tmp.append(temp[j]*2)
                    cont = True
                elif temp[j] != temp[j+1] and cont == False:
                    tmp.append(temp[j])
                elif cont == True:
                    cont = False
            if cont == False and len(temp) >= 1:
                tmp.append(temp[-1])
            for idx, j in enumerate(range(N)):
                if idx < len(tmp):
                    board[i][j] = tmp[idx]
                else:
                    board[i][j] = 0
    else:
        for i in range(N):
            temp = []
            tmp = []
            cont = False
            for j in range(N-1, -1, -1):
                if board[i][j] != 0:
                    temp.append(board[i][j])
            for j in range(len(temp)-1):
                if temp[j] == temp[j+1] and cont == False:
                    tmp.append(temp[j]*2)
                    cont = True
                elif temp[j] != temp[j+1] and cont == False:
                    tmp.append(temp[j])
                elif cont == True:
                    cont = False
            if cont == False and len(temp) >= 1:
                tmp.append(temp[-1])
            for idx, j in enumerate(range(N-1, -1, -1)):
                if idx < len(tmp):
                    board[i][j] = tmp[idx]
                else:
                    board[i][j] = 0
    return board

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dm = ['U', 'D', 'L', 'R']
bf = list(product(dm, 5))
# bf = [['L', 'D', 'L', 'D', 'L']]
result = 0
for case in bf:
    new_board = [row[:] for row in board]
    for mv in case:
        # for i in range(len(new_board)):
        #     print(new_board[i])
        # print()
        new_board = move(new_board, mv)
        # for i in range(len(new_board)):
        #     print(new_board[i])
        # print()
        max_val = max(map(max, new_board))
        if max_val > result:
            result = max_val
print(result)