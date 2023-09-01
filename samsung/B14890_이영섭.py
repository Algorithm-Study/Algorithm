N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

if L == 1:
    for i in range(N):
        tp = board[i][0]
        flag = False
        for j in range(1, N):
            if abs(board[i][j] - tp) >= 2:
                break
            elif tp - board[i][j] == 1:
                flag = True
            elif tp - board[i][j] == -1:
                if flag:
                    break
            elif tp == board[i][j]:
                flag = False
            tp = board[i][j]
        else:
            ans += 1
    for i in range(N):
        tp = board[0][i]
        flag = False
        for j in range(1, N):
            if abs(board[j][i] - tp) >= 2:
                break
            elif tp - board[j][i] == 1:
                flag = True
            elif tp - board[j][i] == -1:
                if flag:
                    break
            elif tp == board[j][i]:
                flag = False
            tp = board[j][i]
        else:
            ans += 1
else:
    # 행
    for i in range(N):
        tp = board[i][0]
        tpc, dc = 1, 0
        flag = False
        # print(i)
        for j in range(1, N):
            # print(j, end=" ")
            if tp == board[i][j]:  # 같을 때
                # print("=", end=" ")
                if flag:
                    dc += 1
                    if dc >= L:
                        flag = False
                else:
                    tpc += 1
                continue
            elif abs(tp - board[i][j]) > 1:  # 2 이상 차이날 때
                # print("2", end=" ")
                break
            elif tp - board[i][j] == -1:  # 올라갈 때
                # print("+", end=" ")
                if tpc < L:
                    break
                tpc = 1
            elif tp - board[i][j] == 1:  # 내려갈 때
                # print("-", end=" ")
                if flag:
                    if dc < L:
                        break
                flag = True
                dc = 1
                tpc = 0

            tp = board[i][j]
        else:
            if not flag:
                ans += 1
    # 열
    for i in range(N):
        tp = board[0][i]
        tpc, dc = 1, 0
        flag = False
        # print(i)
        for j in range(1, N):
            # print(j, end=" ")
            if tp == board[j][i]:  # 같을 때
                # print("=", end=" ")
                if flag:
                    dc += 1
                    if dc >= L:
                        flag = False
                else:
                    tpc += 1
                continue
            elif abs(tp - board[j][i]) > 1:  # 2 이상 차이날 때
                # print("2", end=" ")
                break
            elif tp - board[j][i] == -1:  # 올라갈 때
                # print("+", end=" ")
                if tpc < L:
                    break
                tpc = 1
            elif tp - board[j][i] == 1:  # 내려갈 때
                # print("-", end=" ")
                if flag:
                    if dc < L:
                        break
                flag = True
                dc = 1
                tpc = 0

            tp = board[j][i]
        else:
            if not flag:
                ans += 1
print(ans)
