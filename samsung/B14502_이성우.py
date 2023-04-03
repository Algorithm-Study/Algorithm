from itertools import combinations as cmb
# 변수 설정
R, C = map(int,input().split())
maps_tmp = [list(map(int,input().split())) for _ in range(R)]
# print('-'*2*C)
# for _ in maps:
#     print(*_)
cnt = 0

# 완전 탐색
for cases in cmb(range(R*C),3):
    
    continue_point = False
    maps = [_[:] for _ in maps_tmp]

    # 벽을 설치할 때 바이러스 또는 이미 벽이 있는 공간에 설치하는 것은 제외
    for dot in cases:
        if maps[dot//C][dot%C] == 2 or maps[dot//C][dot%C] == 1:
            continue_point = True
            break
    # 제외 경우가 아니라면 벽 설치
    else:
        # print(cases)
        maps[cases[0]//C][cases[0]%C] = 1
        maps[cases[1]//C][cases[1]%C] = 1
        maps[cases[2]//C][cases[2]%C] = 1
        
    # 한 개라도 예외 경우이면 다음 경우 수 탐색
    if continue_point == True:
        continue
    
    cnt_tmp = 0
    virus = []
    # 탐색 시작할 virus 담기
    for i, u in enumerate(maps):
        for j, v in enumerate(u):
            if v == 2:
                virus.append([i,j])
    # print(virus)
    # print('-'*2*C)
    # for _ in maps:
    #     print(*_)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # bfs로 바이러스 확장
    while virus:
        x, y = virus.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] == 0:
                maps[nx][ny] = 2
                virus.append([nx, ny])
    
    # 안전 공간 count
    for _ in maps:
        for _ in _:
            if _ == 0:
                cnt_tmp += 1
                
    # if cnt_tmp > cnt:
    #     print('-'*2*C,cases)
    #     for _ in maps:
    #         print(*_)      
    
    # 최대값 비교        
    cnt = max(cnt, cnt_tmp)

print(cnt)