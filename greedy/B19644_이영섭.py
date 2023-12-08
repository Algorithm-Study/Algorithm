import sys
input = sys.stdin.readline

L = int(input())
ml, mk = map(int, input().split())
C = int(input())
Z = []
damage = [0]*3000001
for _ in range(L):
    Z.append(int(input()))

for i in range(1, L+1):
    nd = damage[i - 1] - damage[max(0, i - ml)]
    if Z[i-1] <= nd + mk:
        damage[i] = damage[i - 1] + mk
    else:
        if C > 0:
            C -= 1
            damage[i] = damage[i - 1]
        else:
            print("NO")
            exit()
print("YES")
