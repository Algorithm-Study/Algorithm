n, L = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
avail = 0
# 가로 줄 이동 가능 여부 체크
for i in range(n):
    line = field[i]
    visited = [0]*n
    possible = True
    for j in range(1,n):
        # 높이 차가 1을 넘어가는 경우 탐색 불필요
        if abs(line[j] - line[j-1]) > 1:
            break
        # 내려가는 경사로
        if line[j] < line[j-1]:
            for l in range(L):
                if j+l >= n or visited[j+l] or line[j] != line[j+l]:
                    possible = False
                    break
                visited[j+l] = 1
            if not possible:
                break
        # 올라가는 경사로
        elif line[j] > line[j-1]:
            for l in range(L):
                if j-l-1 < 0 or visited[j-l-1] or line[j-1] != line[j-l-1]:
                    possible = False
                    break
                visited[j-l-1] = 1
            if not possible:
                break
    else:
        avail += 1
# 세로 줄 이동 가능 여부 체크
for i in range(n):
    line = [x[i] for x in field]
    visited = [0]*n
    possible = True
    for j in range(1,n):
        # 높이 차가 1을 넘어가는 경우 탐색 불필요
        if abs(line[j] - line[j-1]) > 1:
            break
        # 내려가는 경사로
        if line[j] < line[j-1]:
            for l in range(L):
                if j+l >= n or visited[j+l] or line[j] != line[j+l]:
                    possible = False
                    break
                visited[j+l] = 1
            if not possible:
                break
        # 올라가는 경사로
        elif line[j] > line[j-1]:
            for l in range(L):
                if j-l-1 < 0 or visited[j-l-1] or line[j-1] != line[j-l-1]:
                    possible = False
                    break
                visited[j-l-1] = 1
            if not possible:
                break
    else:
        avail += 1
print(avail)
                