h, w = map(int, input().split())
walls = list(map(int, input().split()))
result = 0
for i in range(1,w-1):
    rain = min(max(walls[:i]), max(walls[i+1:]))
    if walls[i] < rain:
        result += rain - walls[i]
print(result)  