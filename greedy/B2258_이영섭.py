
N, M = map(int, input().split())
meet = []
for _ in range(N):
    w, c = map(int, input().split())
    meet.append((w, c))
meet.sort(key=lambda x: [x[1], -x[0]])

weight = 0
max_c, total = 0, 0
for i in range(N):
    w, c = meet[i]
    if weight < M:
        weight += w
        if max_c == c:
            total += c
        else:
            max_c = c
            total = c
    elif max_c == c:
        continue
    elif total > c:
        total = c
        break
    else:
        break

if weight < M:
    print(-1)
else:
    print(total)
