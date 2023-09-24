from collections import deque
n, k = map(int, input().split())
lab = []
virus_info = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] != 0:
            virus_info.append((lab[i][j], 0, i, j))
s, target_x, target_y = map(int, input().split())
virus_info.sort()
q = deque(virus_info)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, current_s, x, y = q.popleft()
    if s == current_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>= 0 and nx < n and ny>=0 and ny <n:
            if lab[nx][ny] == 0:
                lab[nx][ny] = virus
                q.append((virus, current_s + 1, nx, ny))
print(lab[target_x - 1][target_y - 1])
