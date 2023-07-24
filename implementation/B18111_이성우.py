n, m, b = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]

answer = float('inf')
height = 0

for i in range(257):
    plus_block = 0
    minus_block = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] > i:
                plus_block += arr[x][y] - i
            else:
                minus_block += i - arr[x][y]
                
    if minus_block > plus_block + b:
        continue
    
    tmp = plus_block*2 + minus_block
    
    if tmp <= answer:
        answer = tmp
        height = i
        
print(answer, height)