import sys
input = sys.stdin.readline
n,m = map(int,input().split())

maps = [list(input().rstrip()) for _ in range(n)]

# for _ in maps:
#     print(*_)

# visited = [ [0 for _ in range(m)] for _ in range(n)]
letter = [0]*26
max_depth = 0

def dfs(i,j, letters, depth):
    global max_depth
    if i < 0 or n <= i or j < 0 or m <= j:
        return
    
    if letters[ord(maps[i][j])-65] == 0:
        depth += 1
        letters[ord(maps[i][j])-65] = 1
        # visited[i][j] = max(visited[i][j], depth)
        max_depth = max(max_depth, depth)
        dfs(i-1, j, letters, depth)
        dfs(i, j-1, letters, depth)
        dfs(i+1, j, letters, depth)
        dfs(i, j+1, letters, depth)
        letters[ord(maps[i][j])-65] = 0

dfs(0,0, letter, 0)

# for _ in visited:
#     print(*_)
    
print(max_depth)

# 위의 방법은 탐색 순서에 따라 시간초과가 발생
# 특히 위부터 탐색하면 시간초과..
# bfs, set()로 풀고 python으로 제출하면 훨씬 빠르게 탐색할 수 있다