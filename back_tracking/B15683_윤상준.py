n, m = map(int, input().split())
field = []
cameras = []
results = []
ways = [(-1,0), (0,-1), (1,0), (0,1)]
type = [
    [ ],
    [[0], [1], [2], [3]],
    [[1,3],[0,2]],
    [[0,3],[2,3],[1,2],[0,1]],
    [[0,1,3], [0,2,3],[1,2,3], [0,1,2]],
    [[0,1,2,3]]
]
for i in range(n):
    line = list(map(int, input().split()))
    field.append(line)
    for j in range(m):
        if line[j] in list(range(1,6)):
            cameras.append((line[j], i, j))
# 감시 영역 확인           
def bfs(new_field, cases, x, y):
    for case in cases:
        nx,ny = x,y
        while True:
            nx += ways[case][0]
            ny += ways[case][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or new_field[nx][ny] == 6:
                break
            new_field[nx][ny] = -1
# 백트래킹
def dfs(field,count):
    if count == len(cameras):
        results.append(sum([x.count(0) for x in field]))
        return
    new_field = [x[:] for x in field]
    version,x,y = cameras[count]
    for cases in type[version]:
        bfs(new_field, cases, x, y)
        dfs(new_field, count + 1)
        new_field = [x[:] for x in field]

dfs(field,0)
print(min(results))

# 모든 카메라를 설치했을 때 감지하지 못하는 영역을 저장
# 이후 저장한 기록 중 가장 작은 값 출력