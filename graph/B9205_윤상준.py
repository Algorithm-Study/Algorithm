from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    queue = deque()
    queue.append(list(map(int, input().split())))
    convenience = [list(map(int, input().split())) for _ in range(n)]
    visited = [0]*n
    goal = list(map(int, input().split()))
    while queue:
        x, y = queue.popleft()
        if abs(goal[0] - x) + abs(goal[1] - y) <= 1000:
            print('happy')
            break
        to_remove = []
        for i in range(n):
            if visited[i]:
                continue
            if abs(convenience[i][0] - x) + abs(convenience[i][1] - y) <= 1000:
                queue.append(convenience[i])
                visited[i] = 1
    else:
        print('sad')

# 한칸씩 이동하는 bfs가 아니라 노드를 중심으로 이동하는 bfs 구현하면 됨