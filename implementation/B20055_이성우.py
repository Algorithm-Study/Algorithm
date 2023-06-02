from collections import deque
n, k = map(int, input().split())
arr = deque(map(int, input().split()))
robot = deque([0]*(n*2))
answer = 0
while arr.count(0) < k:
    answer += 1
    
    # 1단계
    arr.rotate(1)
    robot.rotate(1)
    if robot[n-1] != 0:
        robot[n-1] = 0
    
    # 2단계
    for i in range(n)[::-1]:
        if robot[i] != 0 and robot[i+1] == 0 and arr[i+1] >= 1:
            robot[i+1], robot[i] = robot[i], robot[i+1]
            arr[i+1] -= 1        
    if robot[n-1] == 1:
        robot[n-1] = 0
        
    # 3단계
    if arr[0] != 0:
        robot[0] = 1
        arr[0] -= 1

print(answer)