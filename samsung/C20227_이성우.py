from collections import deque, defaultdict

def find_path(n, arr, cord, store_cord):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visited = [[False]*n for _ in range(n)]
    
    q = deque()
    q.append((cord[0], cord[1], 0, [[cord[0], cord[1]]]))
    visited[cord[0]][cord[1]] = 0
    
    cost = n*n + 1
    path = []
    
    while q:
        x, y, c, p = q.popleft()
        if store_cord:
            if x == (store_cord[0]-1) and y == (store_cord[1]-1) and c < cost:
                cost = c
                path = p
            
        else:
            if arr[x][y] == 1 and c < cost:
                cost = c
                path = p
                    
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and arr[nx][ny] != -1:
                n_path = p[:]
                n_path.append([nx, ny])
                q.append([nx, ny, c+1, n_path])
                visited[nx][ny] = True
    
    return path
        
        
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
store = [list(map(int, input().split())) for _ in range(m)]
people = defaultdict(list)

arrived = 0
t = 0

while arrived < m:
    t += 1
    
    for order, cord in people.items():
        if cord[-1] != -1:
            path = find_path(n, arr, cord, store[order])
            if path[1][0] == (store[order][0]-1) and path[1][1] == (store[order][1]-1):
                arr[path[1][0]][path[1][1]] = -1
                people[order][-1] = -1
                arrived += 1
            else:
                people[order] = [path[1][0], path[1][1], 1]
                
    if t <= m:
        store_x, store_y = store[t-1]
        path = find_path(n, arr, [store_x-1, store_y-1], None)
        people[t-1] = [path[-1][0], path[-1][1], 1]
        arr[path[-1][0]][path[-1][1]] = -1
        
print(t)