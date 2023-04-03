# python3 : 33300kb / 1304ms
# pypy3 : 146972kb / 340ms
R, C ,M = map(int,input().split())
shark_list = []
field = [[0]*C for _ in range(R)]
way = [(-1,0),(1,0),(0,1),(0,-1)]
total = 0
# 상어 목록 입력받기 & 맵에 위치 입력하기
for i in range(1,M+1):
    r,c,s,d,z = map(int, input().split())
    shark_list.append([i,r-1,c-1,s,d-1,z])
    field[r-1][c-1] = i  
# 낚시 시작!
for i in range(C):
    #상어 있는지 체크
    #for j in range(R):
    #    print(field[j])
    #print('='*20, i)
    for j in range(R):
        if field[j][i] != 0:
            shark_num = field[j][i]
            total += shark_list[shark_num-1][5]
            shark_list[shark_num-1] = [-1, 0, 0, 0, 0, 0]
            field[j][i] = 0
            break
    #상어 이동 시작
    temp = [[0]*C for _ in range(R)]
    for i in range(len(shark_list)):
        num, nr, nc, ns, nd, nz = shark_list[i]
        speed = ns
        if num == -1:
            continue
        #위로 이동하는 경우
        if nd == 0:
            ns += 2 *(R-1) -nr
            ns = ns%(2*R - 2)
            if ns >= R:
                nr = 2 * R - 2 - ns
            else:
                nr= ns
                nd = 1
            #도착한 상어가 있는지 체크
            if temp[nr][nc] != 0:
                another = temp[nr][nc]
                if shark_list[another-1][5] > nz:
                    shark_list[num-1] = [-1, 0, 0, 0, 0, 0]
                else:
                    shark_list[another-1] = [-1, 0, 0, 0, 0, 0]
                    temp[nr][nc] = num
                    shark_list[num-1] = [num, nr, nc, speed, nd, nz] 
            else:
                temp[nr][nc] = num
                shark_list[num-1] = [num, nr, nc, speed, nd, nz]  
            continue
        elif nd == 1:
            ns += nr
            ns = ns%(2*R - 2)
            if ns >= R:
                nr = 2 * R - 2 - ns
                nd = 0
            else:
                nr = ns
            #도착한 상어가 있는지 체크
            if temp[nr][nc] != 0:
                another = temp[nr][nc]
                if shark_list[another-1][5] > nz:
                    shark_list[num-1] = [-1, 0, 0, 0, 0, 0]
                else:
                    shark_list[another-1] = [-1, 0, 0, 0, 0, 0]
                    temp[nr][nc] = num
                    shark_list[num-1] = [num, nr, nc, speed, nd, nz] 
            else:
                temp[nr][nc] = num
                shark_list[num-1] = [num, nr, nc, speed, nd, nz]
            continue
        elif nd == 2:
            ns += nc
            ns = ns%(2*C - 2)
            if ns >= C:
                nc = 2 * C - 2 - ns
                nd = 3
            else:
                nc = ns
            #도착한 상어가 있는지 체크
            if temp[nr][nc] != 0:
                another = temp[nr][nc]
                if shark_list[another-1][5] > nz:
                    shark_list[num-1] = [-1, 0, 0, 0, 0, 0]
                else:
                    shark_list[another-1] = [-1, 0, 0, 0, 0, 0]
                    temp[nr][nc] = num
                    shark_list[num-1] = [num, nr, nc, speed, nd, nz] 
            else:
                temp[nr][nc] = num
                shark_list[num-1] = [num, nr, nc, speed, nd, nz]
            continue 
        else:
            ns += 2 * (C - 1) - nc
            ns = ns%(2*C - 2)
            if ns >= C:
                nc = 2 * C - 2 - ns
            else:
                nc = ns
                nd = 2
            #도착한 상어가 있는지 체크
            if temp[nr][nc] != 0:
                another = temp[nr][nc]
                if shark_list[another-1][5] > nz:
                    shark_list[num-1] = [-1, 0, 0, 0, 0, 0]
                else:
                    shark_list[another-1] = [-1, 0, 0, 0, 0, 0]
                    temp[nr][nc] = num
                    shark_list[num-1] = [num, nr, nc, speed, nd, nz] 
            else:
                temp[nr][nc] = num
                shark_list[num-1] = [num, nr, nc, speed, nd, nz]
    for k in range(R):
        field[k] = temp[k][:]

print(total)          