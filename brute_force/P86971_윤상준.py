from collections import defaultdict
def find_parent(parent,x):
        if parent[x] == x:
            return x
        return find_parent(parent, parent[x])

def union(parent, x1,x2):
    if find_parent(parent, x1) < find_parent(parent, x2):
        parent[find_parent(parent, x2)] = parent[find_parent(parent, x1)]
    else:
        parent[find_parent(parent, x1)] = parent[find_parent(parent, x2)]
def solution(n, wires):      
    wires.sort(key = lambda x : (x[0], -x[1]))
    answer = 101
    cut = 0
    while cut != n-1:
        parent = [x for x in range(n+1)]
        for i in range(n-1):
            if i == cut:
                continue
            union(parent, wires[i][0], wires[i][1])
        diff = defaultdict(int)
        for i in range(1,n+1):
            diff[find_parent(parent, i)] += 1
        result = list(diff.values())
        answer = min(answer, abs(result[0] - result[1]))
        cut += 1
    return answer

# 집합 관계로 풀려고 했으나 풀리지 않는 케이스가 존재
# union find로 트리 구조 파악해서 문재 헤결하는 것으로 변경