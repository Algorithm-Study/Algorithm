n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
students = [[] for _ in range(n**2+1)]
order = []
for _ in range(n**2):
    prefer = list(map(int, input().split()))
    students[prefer[0]] = prefer[1:]
    order.append(prefer[0])

def check_prefer(num):
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    prefer_arr = [[0 for _ in range(n)] for _ in range(n)]
    prefer_max = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] in students[num]:
                        prefer_arr[x][y] += 1
                prefer_max = max(prefer_max, prefer_arr[x][y])

    blank_arr = [[0 for _ in range(n)] for _ in range(n)]
    blank_max = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0 and prefer_arr[x][y] == prefer_max:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                        blank_arr[x][y] += 1
                blank_max = max(blank_max, blank_arr[x][y])

    for x in range(n):
        for y in range(n):
            if arr[x][y] == 0 and prefer_arr[x][y] == prefer_max and blank_arr[x][y] == blank_max:
                arr[x][y] = num
                return


for number in order:
    check_prefer(number)

answer = 0
score = [0, 1, 10, 100, 1000]
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] in students[arr[x][y]]:
                cnt += 1
                
        answer += score[cnt]

print(answer)