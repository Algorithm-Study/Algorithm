n= int(input())
field = [[0]*(n+1) for _ in range(n+1)]
favorite = [[0,0,0,0] for _ in range(n**2 + 1)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 순차적으로 학생 배치
for _ in range(n**2):
    student, f1, f2, f3, f4 = map(int, input().split())
    cases = []
    for x in range(1,n+1):
        for y in range(1,n+1):
            if field[x][y] == 0:
                f_cnt, e_cnt = 0, 0
                for i in range(4):
                    nx = x+ dx[i]
                    ny = y+ dy[i]
                    if nx < 1 or ny < 1 or nx >=n+1 or ny >=n+1:
                        continue
                    if field[nx][ny] in (f1,f2,f3,f4):
                        f_cnt += 1
                    if field[nx][ny] == 0:
                        e_cnt += 1
                cases.append((f_cnt,e_cnt,x,y))
    cases.sort(key =  lambda x: (-x[0], -x[1], x[2], x[3]))
    field[cases[0][2]][cases[0][3]] = student
    favorite[student] = [f1,f2,f3,f4]
# 배치가 완료된 이후 인접하게 된 좋아하는 사람 수를 다시 구해야함
total = 0
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
for x in range(1,n+1):
    for y in range(1,n+1):
        f_cnt = 0
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx < 1 or ny < 1 or nx >=n+1 or ny >=n+1:
                continue
            if field[nx][ny] in favorite[field[x][y]]:
                f_cnt += 1
        total += score[f_cnt]
print(total)