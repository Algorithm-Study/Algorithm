import sys
input = sys.stdin.readline

N = int(input())
building = list(map(int,input().split()))
answer = 0

def gradient(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)


for idx, b in enumerate(building):
    cnt = 0
    l_gradient = float('inf')
    r_gradient = -float("inf")
    
    for i in range(idx-1, -1, -1):
        grad = gradient(idx+1, b, i+1, building[i]) 
        if grad < l_gradient:
            l_gradient = grad 
            cnt += 1
            
    for i in range(idx+1, N):
        grad = gradient(idx+1, b, i+1, building[i])
        if grad > r_gradient:
            r_gradient = grad
            cnt += 1
            
    answer = max(answer, cnt)
    
print(answer)