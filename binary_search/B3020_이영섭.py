import sys
input = sys.stdin.readline

N, H = map(int, input().split())
jongyuseok = [0]*(H+2)
seoksoon = [0]*(H+2)
for i in range(N):
    temp = int(input().rstrip())
    if i % 2 == 0:
        seoksoon[temp] += 1
    else:
        jongyuseok[H+1-temp] += 1
val = 0
for i in range(1, H+1):
    val += jongyuseok[i]
    jongyuseok[i] = val

val = 0
for i in range(H, 0, -1):
    val += seoksoon[i]
    seoksoon[i] = val
ans = 200001
cnt = 1
for i in range(1, H+1):
    if ans > jongyuseok[i] + seoksoon[i]:
        ans = jongyuseok[i] + seoksoon[i]
        cnt = 1
    elif ans == jongyuseok[i] + seoksoon[i]:
        cnt += 1
print(ans, cnt)