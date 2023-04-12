INF = 1e8
command = list(map(int, input().split()))
foot = [[[INF]*5 for _ in range(5)] for _ in range(len(command)-1)]

for i in range(1, len(command)):
    move = command[i-1]