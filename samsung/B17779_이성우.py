import sys
input = sys.stdin.readline

def cal(x, y, d1, d2):
    section = [0]*5
    
    tmp = y
    for i in range(x+d1):
        if i >= x:
            tmp -= 1
        section[0] += sum(arr[i][:tmp+1])

    tmp = y+1
    for i in range(x+d2+1):
        if i > x:
            tmp += 1
        section[1] += sum(arr[i][tmp:])

    tmp = y-d1-1
    for i in range(x+d1, n):
        section[2] += sum(arr[i][:tmp+1])
        if i < x+d1+d2:
            tmp += 1

    tmp = y+d2
    for i in range(x+d2+1, n):
        section[3] += sum(arr[i][tmp:])
        if i <= x+d1+d2:
            tmp -= 1

    section[4] = total - sum(section)
    return max(section) - min(section)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
total = sum(map(sum, arr))
answer = float('inf')

for x in range(n):
    for y in range(n):
        for d1 in range(1, y+1):
            for d2 in range(1, n-y+1):
                if x+d1+d2 < n and 0 <= y-d1 and y+d2 < n:
                    answer = min(answer, cal(x, y, d1, d2))
                else:
                    break

print(answer)