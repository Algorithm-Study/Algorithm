from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))
belt1, belt2 = deque(reversed(data[:n])), deque(reversed(data[n:]))
robot = deque([0]*n)
count, result = 0, 0

while count < k:
    result += 1
    belt2.append(belt1.popleft())
    belt1.append(belt2.popleft())
    robot.popleft()
    robot.append(0)
    if robot[0] == 1:
        robot[0] = 0
    if sum(robot):
        for i in range(1, n):
            if robot[i] == 1 and robot[i-1] == 0 and belt1[i-1] > 0:
                belt1[i-1] -= 1
                if belt1[i-1] == 0:
                    count += 1
                robot[i], robot[i-1] = 0, 1
    if belt1[-1] > 0:
        belt1[-1] -= 1
        if belt1[-1] == 0:
            count += 1
        robot[-1] = 1
print(result)