n = int(input())
count = 0
info = []
for _ in range(n):
    pos, people = map(int, input().split())
    count += people
    info.append((pos,people))
info.sort()
current = 0
for _ in range(n):
    current += info[_][1]
    if current >= count/2:
        print(info[_][0])
        break