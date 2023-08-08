n = int(input())

arr = [[0]*101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):

    y, x, d, g = map(int, input().split())
    arr[x][y] = 1

    curve = [d]
    for _ in range(g):
        for k in range(len(curve))[::-1]:
            curve.append((curve[k]+1) % 4)

    for j in range(len(curve)):
        x += dx[curve[j]]
        y += dy[curve[j]]
        if 0 <= x < 101 and 0 <= y < 101:
            arr[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            answer += 1

print(answer)