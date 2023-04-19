from collections import deque
t = int(input())
start = []
end = []
# 레지스터 형태라서 0100 같은 케이스의 전환이 잘 되는지 확인해야 함
for i in range(t):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)
for i in range(t):
    queue = deque()
    visited = [0 for _ in range(10000)]
    queue.append([start[i], ''])
    while queue:
        value, op = queue.popleft()
        visited[value] = 1
        if value == end[i]:
            print(op)
            break
        # D인 경우
        temp = value*2
        if temp > 9999:
            temp = temp % 10000
        if visited[temp] == 0:
            queue.append([temp, op+'D'])
            visited[temp] = 1
        # S인 경우
        temp = value - 1
        if temp == -1:
            temp = 9999
        if visited[temp] == 0:
            queue.append([temp, op+'S'])
            visited[temp] = 1
        # L인 경우
        temp = (value*10 + (value//1000))%10000
        if visited[temp] == 0:
            queue.append([temp, op+'L'])
            visited[temp] = 1
        # R인 경우
        temp = ((value%10)*1000 + value//10)%10000
        if visited[temp] == 0:
            queue.append([temp, op+'R'])
            visited[temp] = 1
    