import sys
input = sys.stdin.readline

# 유니온 파인드 구현
def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
        
# 초기값 설정
n, m = map(int, input().split())
parent = [_ for _ in range(n+1)]
answer = 0
arr = []
last_edge = []

# 유지비 순으로 정렬
for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])
arr.sort(key=lambda x: x[0])

# 유니온 파인드 실행
for c, a, b in arr:
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        union(a, b)
        answer += c
        last_edge.append(c)

# 마지막 간선을 끊어서 마을 두개로 분리 후 정답 프린트
answer -= last_edge.pop()
print(answer)