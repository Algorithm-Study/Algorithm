N = int(input())
town = []
people = 0
for _ in range(N):
    x, a = map(int, input().split())
    people += a
    town.append((x, a))
town.sort()

p = 0
for i in range(N):
    p += town[i][1]
    if p >= people/2:
        print(town[i][0])
        break
