# 느리지만 풀리는 정답
import sys, heapq
way = [[-1,0],[0,-1],[1,0],[0,1]]
curve = [(0,1),(0,3),(2,1),(2,3),(1,0),(3,0),(1,2),(3,2)]
def solution(board):
    n = len(board)
    c_board = [[sys.maxsize]*n for _ in range(n)]
    queue = []
    heapq.heappush(queue,(0,0,0,-1))
    c_board[0][0] = 0
    while queue:
        cost,x,y,before = heapq.heappop(queue)
        if x == n-1 and y == n-1:
            continue
        for i in range(4):
            nx = x + way[i][0]
            ny = y + way[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >=n or board[nx][ny] == 1:
                continue
            new_cost = cost + 100
            if (before,i) in curve:
                new_cost += 500
            if new_cost <= c_board[nx][ny]:
                c_board[nx][ny] = new_cost
                heapq.heappush(queue,(new_cost,nx,ny,i))
            # 테케에서 오차범위를 300까지 설정하면 아래 코드와 비슷한 속도로 통과하면서 정답
            elif new_cost <= c_board[nx][ny] + 500:
                heapq.heappush(queue,(new_cost,nx,ny,i))
    return c_board[n-1][n-1]
# 각 이동 구간별 최솟값으로 진행하면 답에 도달하지 못하는 케이스 존재
# 문제 풀이 단계
# bfs
# bfs + heapq
# bfs + dijkstra
# bfs + dijkstra + 예외 처리
#================================================================
# 빠른 정답 3차원 배열 활용
import sys, heapq
way = [[-1,0],[0,-1],[1,0],[0,1]]
curve = [(0,1),(0,3),(2,1),(2,3),(1,0),(3,0),(1,2),(3,2)]
def solution(board):
    n = len(board)
    c_board = [[[sys.maxsize]*n for _ in range(n)] for _ in range(4)]
    queue = []
    heapq.heappush(queue,(0,0,0,-1))
    c_board[0][0][0], c_board[1][0][0], c_board[2][0][0], c_board[3][0][0] = 0,0,0,0
    while queue:
        cost,x,y,before = heapq.heappop(queue)
        if x == n-1 and y == n-1:
            continue
        for i in range(4):
            nx = x + way[i][0]
            ny = y + way[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >=n or board[nx][ny] == 1:
                continue
            new_cost = cost + 100
            if (before,i) in curve:
                new_cost += 500
            if new_cost <= c_board[i][nx][ny]:
                c_board[i][nx][ny] = new_cost
                heapq.heappush(queue,(new_cost,nx,ny,i))
    return min(c_board[0][n-1][n-1], c_board[1][n-1][n-1], c_board[2][n-1][n-1], c_board[3][n-1][n-1])