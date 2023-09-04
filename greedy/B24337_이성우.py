N, a, b = map(int, input().split())
tmp = []

for i in range(1, a):
    tmp.append(i)
tmp.append(max(a, b))
for i in range(b-1, 0, -1):
    tmp.append(i)

if len(tmp) > N:
    print(-1)
else:
    answer = [tmp[0]]
    for i in range(N-len(tmp)):
        answer.append(1)
    print(*answer+tmp[1:])