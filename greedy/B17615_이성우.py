n = int(input())
arr = list(input())
blue = []
red = []

for idx, color in enumerate(arr):
    if color == 'R':
        red.append(idx+1)
    else:
        blue.append(idx+1)
        
if len(red) == 0 or len(blue) == 0:
    print(0)
    exit()

answer = min(n-len(blue)+1-blue[0],
             blue[-1]-len(blue),
             n-len(red)+1-red[0],
             red[-1]-len(red))

print(answer)