import sys
input = sys.stdin.readline
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(a,b):
    p1,p2 = find(a),find(b)
    if p1 != p2:
        parent[p2] = p1
        friend[p1] += friend[p2]
t = int(input())
for _ in range(t):
    f = int(input())
    parent = {}
    friend = {}
    for _ in range(f):
        a, b = input().split()
        if a not in friend:
            friend[a] = 1
            parent[a]= a
        if b not in friend:
            friend[b] = 1
            parent[b] = b
        union(a,b)
        print(friend[find(a)])
# 숫자로만 하던 분리 집합에서 문자 단위의 분리 집합 진행
# 딕셔너리로 진행하지 않으면 python의 경우 시간 초과 발생
# 출력 초과는 단순히 입력이 많은 것이 아니라 입력 자리수가 정답보다 많으면 발생(정답: 5 제출: 10 -> 출력 초과)