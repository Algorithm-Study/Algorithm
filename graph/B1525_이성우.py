from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(start):
    q = deque()
    q.append(start)
    board[start] = 0
    
    while q:
        now = q.popleft()
        if now == '123456780':
            return board[now]
        idx = now.find('0')
        x, y = idx // 3, idx % 3
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            nidx = nx * 3 + ny
            if 0 <= nx < 3 and 0 <= ny < 3:
                now_list = list(now)
                now_list[idx], now_list[nidx] = now_list[nidx], now_list[idx]
                next = ''.join(now_list)
                if not board.get(next):
                    board[next] = board[now] + 1
                    q.append(next)
    return -1
    
    
board = {}
now_input = input() + input() + input()
now_input = now_input.replace(' ', '')
print(bfs(now_input))