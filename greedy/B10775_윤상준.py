g = int(input())
p = int(input())
gates = [x for x in range(g+1)]
total = 0
planes = [int(input()) for _ in range(p)]
def parent(x):
    if gates[x] == x:
        return x
    p = parent(gates[x])
    gates[x] = p
    return gates[x]

def union(x,y):
    x = parent(x)
    y = parent(y)
    if x < y:
        gates[y] = x
    else:
        gates[x] = y
for i in range(p):
    x = parent(planes[i])
    if x == 0:
        break
    union(x,x-1)
    total += 1
print(total)
# bisect로 접근하면 시간초과
# 분리집합인 Union - find를 활용해야 함