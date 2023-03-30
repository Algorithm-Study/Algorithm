import sys
from copy import deepcopy
input = sys.stdin.readline

# INPUT
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 위로 미는 경우
def up(field):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if field[i][j]:
                tmp = field[i][j]
                field[i][j] = 0
                # 포인터가 가리키는 수가 0일 때
                if field[pointer][j] == 0:
                    field[pointer][j] = tmp
                # 포인터가 가리키는 수와 현재 위치의 수가 같을 때
                elif field[pointer][j]  == tmp:
                    field[pointer][j] *= 2
                    pointer += 1
                # 포인터가 가리키는 수와 현재 위치의 수가 다를 때
                else:
                    pointer += 1
                    field[pointer][j] = tmp
    return field

# 아래로 미는 경우
def down(field):
    for j in range(n):
        pointer = n - 1
        for i in range(n - 2, -1, -1):
            if field[i][j]:
                tmp = field[i][j]
                field[i][j] = 0
                if field[pointer][j] == 0:
                    field[pointer][j] = tmp
                elif field[pointer][j]  == tmp:
                    field[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    field[pointer][j] = tmp
    return field

# 왼쪽으로 미는 경우
def left(field):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if field[i][j]:
                tmp = field[i][j]
                field[i][j] = 0
                if field[i][pointer] == 0:
                    field[i][pointer] = tmp
                elif field[i][pointer]  == tmp:
                    field[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    field[i][pointer]= tmp
    return field

# 우측으로 미는 경우
def right(field):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if field[i][j]:
                tmp = field[i][j]
                field[i][j] = 0
                if field[i][pointer] == 0:
                    field[i][pointer] = tmp
                elif field[i][pointer]  == tmp:
                    field[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    field[i][pointer] = tmp
    return field


# DFS
def dfs(field, cnt):
    if cnt == 5:
        return max(map(max, field))
    return max(dfs(up(deepcopy(field)), cnt + 1), dfs(down(deepcopy(field)), cnt + 1), dfs(left(deepcopy(field)), cnt + 1), dfs(right(deepcopy(field)), cnt + 1))

print(dfs(field, 0))