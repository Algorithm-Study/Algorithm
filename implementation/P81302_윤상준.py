def solution(places):
    answer = [1] * len(places)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for idx, place in enumerate(places):
        for i in range(5):
            for j in range(5):
                count = 0
                if place[i][j] == 'P':
                    # 상하좌우
                    for k in range(4):
                        nx, ny = i+dx[k], j+dy[k]
                        if nx < 0 or nx >= 5 or ny < 0 or ny >=5:
                            continue
                        if place[nx][ny] == 'P':
                            count += 1
                    # 대각 상하좌우
                    if i-1 >= 0 and j-1 >= 0:
                        if place[i-1][j-1] == 'P' and (place[i-1][j] == 'O' or place[i][j-1] == 'O'):
                            count += 1
                    if i-1 >= 0 and j+1 < 5:
                        if place[i-1][j+1] == 'P' and (place[i-1][j] == 'O' or place[i][j+1] == 'O'):
                            count += 1
                    if i+1 < 5 and j-1 >= 0:
                        if place[i+1][j-1] == 'P' and (place[i+1][j] == 'O' or place[i][j-1] == 'O'):
                            count += 1
                    if i+1 < 5 and j+1 < 5:
                        if place[i+1][j+1] == 'P' and (place[i+1][j] == 'O' or place[i][j+1] == 'O'):
                            count += 1
                    # 상하좌우 거리 2
                    if i-2 >= 0:
                        if place[i-2][j] == 'P' and place[i-1][j] == 'O':
                            count += 1
                    if j-2 >= 0:
                        if place[i][j-2] == 'P' and place[i][j-1] == 'O':
                            count += 1
                    if i+2 < 5:
                        if place[i+2][j] == 'P' and place[i+1][j] == 'O':
                            count += 1
                    if j+2 < 5:
                        if place[i][j+2] == 'P' and place[i][j+1] == 'O':
                            count += 1
            
                if count > 0:
                    answer[idx] = 0
    return answer

# 완전 노가다로 문제 해결...