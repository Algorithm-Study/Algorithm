import sys
sys.setrecursionlimit = 10e6

n = int(input())
arr = [int(input()) for _ in range(n)]

def check(arr):
    if len(arr) < 4:
        return arr
    start = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[start] == arr[i]:
            cnt += 1
        else:
            if cnt >= 4:
                arr = arr[:start] + arr[start + cnt:]
                arr = check(arr)
                return arr
            else:
                start = i
                cnt = 1
    else:
        if cnt >= 4:
                arr = arr[:start] + arr[start + cnt:]
                arr = check(arr)
    return arr

answer = n
for i in range(n):
    for j in range(1, 4):
        tmp = arr[:i] + [j] + arr[i+1:]
        answer = min(answer, len(check(tmp)))
            
print(answer)