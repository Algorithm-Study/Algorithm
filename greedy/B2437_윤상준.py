n = int(input())
weights = sorted(list(map(int, input().split())))
goal = 1
for weight in weights:
    if goal < weight:
        break
    goal += weight
print(goal)