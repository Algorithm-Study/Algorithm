import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [1 for _ in range(2*m-1)]

for _ in range(n):
    z, o, t = map(int, input().split())
        
    for i in range(z, z+o):
        arr[i] += 1
        
    for i in range(z+o, 2*m-1):
        arr[i] += 2
                
for i in range(m):
    for j in range(m):
        if j == 0:
            print(arr[m-i-1], end = ' ')
        else:
            print(arr[m+j-1], end = ' ')
    print()
    
# 제일 위의 값과 같으므로 한 줄만 계산하면 된다