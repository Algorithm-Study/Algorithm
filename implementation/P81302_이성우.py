def solution(places: list) -> list:
    answer = []
    def check(x: int,y: int,place: list) -> int:
        dir1 = [[0,1],[1,0],[0,-1],[-1,0]]
        dir2 = [[0,2],[2,0],[0,-2],[-2,0]]
        dir3 = [[1,1],[1,-1],[-1,1],[-1,-1]]
        for i in dir1:
            nx, ny = x+i[0], y+i[1]
            if 0 <= nx < 5 and 0<= ny < 5 and place[nx][ny] == 'P':
                return 1
            
        for i in dir2:
            nx, ny = x+i[0], y+i[1]
            if 0 <= nx < 5 and 0<= ny < 5 and place[nx][ny] == 'P':
                if place[x+i[0]//2][y+i[1]//2] == 'O':
                    return 1
                
        for i in dir3:
            nx, ny = x+i[0], y+i[1]
            if 0 <= nx < 5 and 0<= ny < 5 and place[nx][ny] == 'P':
                if place[x+i[0]][y] == 'O' or place[x][y+i[1]] == 'O':
                    return 1
        return 0
    
    for place in places:
        c = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    c += check(i,j,place)
                    if c:
                        break
            if c > 0:
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer