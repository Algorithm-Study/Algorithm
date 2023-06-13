import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    arr = []
    for _ in range(n):
        x, y = map(int, input().split())
        arr.append([x, y])
    end_x , end_y = map(int ,input().split())
    arr.append([end_x, end_y])
    visited = [False]*(n+1)
    def bfs():
        q = deque()
        q.append((start_x, start_y))
        while q:
            x, y = q.popleft()
            if abs(x - end_x) + abs(y - end_y) <= 1000:
                print('happy')
                return
            for i in range(n):
                if not visited[i]:
                    nx, ny = arr[i]
                    if abs(x-nx) + abs(y-ny) <= 1000:
                        q.append((nx, ny))
                        visited[i] =True
        print('sad')
        return
    bfs()