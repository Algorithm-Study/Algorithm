dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def on_board(stu):
    temp = []
    for i in range(n):
        for j in range(n):
            cnt, blank = 0, 0
            if board[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[nx][ny] in stu:
                        cnt += 1
                    if board[nx][ny] == 0:
                        blank += 1
                    temp.append([cnt, blank, i, j])
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    board[temp[0][2]][temp[0][3]] = stu[0]


def sum_point():
    point = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] in dict_st[board[i][j]]:
                    cnt += 1
            if cnt > 0:
                point += 10**(cnt-1)
    return point


n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
student = [list(map(int, input().split())) for _ in range(n**2)]
dict_st = [[] for _ in range(n**2+1)]
for st in student:
    on_board(st)
    # for i in range(n):
    #     print(board[i])
    # print()
    dict_st[st[0]] = [st[1], st[2], st[3], st[4]]
# print(dict_st)
print(sum_point())

# 문제 접근 방법
# # cnt와 blank를 이용하여 주위의 값을 파악하고
# # 이를 i, j와 함께 배열에 담아 마지막에 sort하여 0번째 idx 값을 추출