n, m =map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def check(arr):
    for i in range(1, n):
        if abs(arr[i] - arr[i-1]) > 1:
            return False
        
        if arr[i] < arr[i-1]:
            for j in range(m):
                if i + j >= n or arr[i] != arr[i+j] or slope[i+j]:
                    return False
                if arr[i] == arr[i+j]:
                    slope[i+j] = True
        elif arr[i] > arr[i-1]:
            for j in range(m):
                if i-j-1 < 0 or arr[i-1] != arr[i-j-1] or slope[i-j-1]:
                    return False
                if arr[i-1] == arr[i-j-1]:
                    slope[i-j-1] = True
    return True

for i in range(n):
    slope = [False]*n
    if check([arr[i][j] for j in range(n)]):
        answer += 1
        
for j in range(n):
    slope = [False]*n
    if check([arr[i][j] for i in range(n)]):
        answer += 1
        
print(answer)