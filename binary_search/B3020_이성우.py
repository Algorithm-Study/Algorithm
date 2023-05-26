width, height = map(int, input().split())
up = [0]*(height+1)
down = [0]*(height+1)

min_val = width
min_count = 0

for idx in range(width):
    num = int(input())
    if idx%2:
        up[num] += 1
    else:
        down[num] += 1
        
for idx in range(height-1)[::-1]:
    up[idx] += up[idx+1]
    down[idx] += down[idx+1]
    
for idx in range(1, height+1):
    if min_val > down[idx] + up[height-idx+1]:
        min_val = down[idx] + up[height-idx+1]
        min_count = 1
    elif min_val == down[idx] + up[height-idx+1]:
        min_count += 1

print(min_val, min_count)