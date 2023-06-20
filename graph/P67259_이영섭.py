from heapq import heappop, heappush
from sys import maxsize

def solution(board):
    N = len(board)
    costBoard = [[ [maxsize] * N for _ in range(N) ] for _ in range(4)]
    for i in range(4): costBoard[i][0][0] = 0
    
    # BFS
    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while heap:
        cost, x, y, d = heappop(heap)
        
        # 4방향 이동
        for dx, dy, dd in ((1,0,0),(-1,0,1),(0,1,2),(0,-1,3)):
            nx, ny = x + dx, y + dy
            
            # 경계 침범 or 벽
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[ny][nx]: continue
            
            # 이동비용 갱신
            newCost = cost + (100 if d == dd else 600)
            
            # 최소비용 갱신
            if costBoard[dd][ny][nx] > newCost:
                costBoard[dd][ny][nx] = newCost
                heappush(heap, (newCost,nx,ny,dd))
                
    return min(costBoard[0][N-1][N-1], costBoard[1][N-1][N-1], costBoard[2][N-1][N-1], costBoard[3][N-1][N-1])