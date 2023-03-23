N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
directions = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
cloud = [[N-2,0],[N-2,1],[N-1,0],[N-1,1]]
water_add_bug = [[-1,-1],[1,-1],[-1,1],[1,1]]

for _ in range(M):
    visited = [[False]*N for _ in range(N)]
    direction, cnt = map(int,input().split())
    add_direction = [direction*c for direction, c in zip(directions[direction-1],[cnt,cnt])]
    temp = []
    for cloud_x, cloud_y in cloud:
        cloud_x = (cloud_x + add_direction[0]) % N
        cloud_y = (cloud_y + add_direction[1]) % N
        temp.append([cloud_x,cloud_y])
        visited[cloud_x][cloud_y] = True
        maps[cloud_x][cloud_y] += 1

    for coordi in temp:
        x, y = coordi
        add_water = 0
        for bug_coordi in water_add_bug:
            nx = x + bug_coordi[0]
            ny = y + bug_coordi[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            else:
                if maps[nx][ny] > 0:
                    add_water += 1
        maps[x][y] += add_water
        
    new_cloud = []

    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and visited[i][j] == False:
                new_cloud.append([i,j])
                maps[i][j] -= 2

    cloud = new_cloud

print(sum(sum(answer) for answer in maps))