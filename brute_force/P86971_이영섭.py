from collections import deque


def bfs(board, st, n):
    visit = [0] * (n+1)
    dq = deque([st])
    visit[st], cnt = 1, 1
    while dq:
        c = dq.popleft()
        for dir in board[c]:
            if not visit[dir]:
                dq.append(dir)
                visit[dir] = 1
                cnt += 1
    return cnt


def solution(n, wires):
    answer = n
    board = [[] for _ in range(n+1)]
    for st, ed in wires:
        board[st].append(ed)
        board[ed].append(st)
        
    for st, ed in wires:
        board[st].remove(ed)
        board[ed].remove(st)
    
        answer = min(answer, abs(bfs(board, st, n) - bfs(board, ed, n)))
        
        board[st].append(ed)
        board[ed].append(st)
        
    return answer

# 문제 접근 방법
# # 하나씩 자르면서 bfs로 몇개씩 연결되어 있는지 파악