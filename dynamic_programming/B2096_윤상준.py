N = int(input())
min_data = [0,0,0]
max_data = [0,0,0]
for _ in range(N):
    line = list(map(int, input().split()))
    min_temp = [0,0,0]
    max_temp = [0,0,0]
    for j in range(3):
        if j == 0:
            min_temp[j] = min(min_data[j], min_data[j+1]) + line[j]
            max_temp[j] = max(max_data[j], max_data[j+1]) + line[j]
        elif j == 1:
            min_temp[j] = min(min_data) + line[j]
            max_temp[j] = max(max_data) + line[j]
        else:
            min_temp[j] = min(min_data[j], min_data[j-1]) + line[j]
            max_temp[j] = max(max_data[j], max_data[j-1]) + line[j]
    min_data = min_temp[:]
    max_data = max_temp[:]
print(max(max_data), end = ' ')
print(min(min_data))