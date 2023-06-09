import sys
n, m = map(int, input().split())
visited = [[0]*n for _ in range(n)]
# 집과 치킨집 저장하기
houses = []
stores = []
m_stores = []
for i in range(n):
    lines = list(map(int, input().split()))
    for j in range(n):
        if lines[j] == 1:
            houses.append((i,j))
        elif lines[j] == 2:
            stores.append((i,j))
# 거리 계산
distances = []
def distance():
    current = 0
    for x,y in houses:
        length = sys.maxsize
        for _, (dx,dy) in m_stores:
            length = min(length, abs(x-dx) + abs(y-dy))
        current += length
    distances.append(current)

# 치킨집 m개 선택하기
def select(count):
    if count == m:
        distance()
        return
    for idx, (x,y) in enumerate(stores):
        if visited[x][y] == 0:
            if m_stores:
                if idx < m_stores[-1][0]:
                    continue
            visited[x][y] = 1
            m_stores.append((idx, (x, y)))
            select(count + 1)
            visited[x][y] = 0
            m_stores.pop()

select(0)
print(min(distances))

# 백트래킹을 구현하는 것보다 조합을 활용해서 모든 경우의 수의 거리 중 최솟값을 출력하는 방식이 더 쉬움