n = int(input())
light_num = int(input())
lights = list(map(int, input().split()))
max_height = max(lights[0]- 0, n - lights[light_num-1])
for i in range(1,light_num):
    distance = lights[i] - lights[i-1]
    if distance % 2 != 0:
        temp = distance // 2 + 1
    else:
        temp = distance // 2
    max_height = max(max_height, temp)
print(max_height)