g = int(input())
p = int(input())
answer = 0
parent = [_ for _ in range(g+1)]
planes = [int(input()) for _ in range(p)]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
for plane in planes:
    gate = find(plane)
    if gate == 0:
        break
    parent[gate] = parent[gate-1]
    answer += 1
print(answer)