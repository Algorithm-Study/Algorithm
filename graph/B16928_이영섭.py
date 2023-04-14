from collections import deque

N, M = map(int, input().split())
board = [0 for i in range(101)]
sadari = {}
for i in range(N):
    x, y = map(int, input().split())
    sadari[x] = y
snake = {}
for i in range(M):
    u, v, = map(int, input().split())
    snake[u] = v


def bfs():
    dq = deque()
    dq.append(1)
    board[1] = 1
    while dq:
        num = dq.popleft()
        for i in range(1, 7):
            nn = num + i
            if nn < 0 or nn >= 101 or board[nn] > 0:
                continue
            if nn == 100:
                return board[num]
            if nn in sadari:
                if board[sadari[nn]] > 0:
                    continue
                dq.append(sadari[nn])
                board[sadari[nn]] = board[num] + 1
            elif nn in snake:
                if board[snake[nn]] > 0:
                    continue
                dq.append(snake[nn])
                board[snake[nn]] = board[num] + 1
            else:
                dq.append(nn)
                board[nn] = board[num] + 1


print(bfs())

# 문제 접근 방법
# # dp인가 싶었지만 뱀이 내려오는 경우에 최솟값이 존재할 수도 있으므로
# # 단방향 그래프가 아니기 때문에 dp는 사용하기 어려움
# # 최단거리를 구할 때, bfs로 너비 우선 탐색 가능