def run(x):
    cx = x
    while True:
        visit[cx] = x
        cx = student[cx]
        if visit[cx] == x:
            while visit[cx] != -1:
                visit[cx] = -1
                cx = student[cx]
            return
        elif visit[cx] != 0:
            return


T = int(input())
for _ in range(T):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visit, cnt = [0] * (n+1), 0
    for i in range(1, n+1):
        if visit[i] == 0:
            run(i)
    for i in range(1, n+1):
        if visit[i] != -1:
            cnt += 1
    print(cnt)