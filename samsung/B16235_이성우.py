import heapq
import sys
input = sys.stdin.readline

# 시간초과 풀이

def spring(trees):
    # 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가
    # 가장 어린 나무부터 양분을 먹고
    # 양분을 먹을 수 없다면 나무는 죽는다
    growth = [[[] for _ in range(n)] for _ in range(n)]
    death = []
    for i in range(n):
        for j in range(n):
            while trees[i][j]:
                tree = heapq.heappop(trees[i][j])
                if arr[i][j] < tree:
                    death.append([i, j, tree])
                    while trees[i][j]:
                        death.append([i, j, trees[i][j].pop()])
                else:
                    arr[i][j] -= tree
                    heapq.heappush(growth[i][j], tree+1)
    
    return growth, death


def summer(arr, death):
    # 죽은 나무는 그 자리에서 나이//2의 양분으로 변한다
    for i, j, d in death:
        arr[i][j] += d//2
                
    return arr


def fall(trees):
    # 나이가 5의 배수인 나무는 주변으로 번식한다
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            for t in trees[i][j]:
                if t%5 == 0:
                    for idx in range(8):
                        ni = i + di[idx]
                        nj = j + dj[idx]
                        if 0 <= ni < n and 0 <= nj < n:
                            heapq.heappush(trees[ni][nj], 1)
                            
    return trees


def winter(arr):
    # 맵에 비료가 추가된다
    for i in range(n):
        for j in range(n):
            arr[i][j] += fert[i][j]
            
    return arr


n, m, k = map(int, input().split())
fert = [list(map(int, input().split())) for _ in range(n)]
arr = [[5 for _ in range(n)] for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j, age = map(int, input().split())
    heapq.heappush(trees[i-1][j-1], age)

for _ in range(k):
    trees, death = spring(trees)
    arr = summer(arr, death)
    trees = fall(trees)
    arr = winter(arr)

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)