from sys import stdin, maxsize
from itertools import combinations
from copy import deepcopy

def solution(N, M, graph):
    # int 최대값을 가져오는 sys.maxsize
    answer = maxsize
    virus = [(x,y) for y in range(N) for x in range(N) if graph[y][x] == 2] # 모든 바이러스 위치
    totalCount = sum([g.count(0) for g in graph]) # 연구소 빈칸의 개수

    # 바이러스 확산
    def spreadVirus(stack):
        newStack = set()
        for x, y in stack:
            for dx, dy in ((1,0), (0,1), (-1,0), (0,-1)):
                nx, ny = x + dx , y + dy
                if 0 <= nx < N and 0 <= ny < N and (newGraph[ny][nx] == 0 or newGraph[ny][nx] == 2):
                    newStack.add((nx, ny))
        return newStack
    
    # 바이러스 경우의 수 계산
    for case in combinations(range(len(virus)), M):
        stack = set([virus[i] for i in case])
        newGraph = deepcopy(graph)
        second = -1
        count = totalCount
        while stack:
            second += 1
            # 가지치기
            if second >= answer: break
            # 연구소의 모든 빈 칸 바이러스 검증
            if count == 0:
                answer = min(answer, second)
                break
            # 바이러스 확산 범위
            stack = spreadVirus(stack)
            # 바이러스 확산
            for x, y in stack:
                if newGraph[y][x] == 0:
                    count -= 1
                newGraph[y][x] = 1

    return answer if answer != maxsize else -1

N, M = map(int,stdin.readline().split())
graph = list(list(map(int,stdin.readline().split())) for _ in range(N))

res = solution(N, M, graph)
print(res)