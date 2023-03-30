def solution(park, routes):
    # 변수 설정
    arr = [[_ for _ in _] for _ in park]
    r, c = len(arr), len(arr[0])
    direction_dict = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    
    # 시작 위치 찾기
    for i, values in enumerate(arr):
        for j, value in enumerate(values):
            if value == 'S':
                x, y = i, j
                
    # 주어진 방향과 거리를 한칸씩 움직이고 갈 수 있으면 변경점 적용
    for route in routes:
        direction, move = route.split()
        tmp_x, tmp_y = x, y
        for _ in range(int(move)):
            nx = tmp_x + direction_dict[direction][0]
            ny = tmp_y + direction_dict[direction][1]

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != 'X':
                tmp_x, tmp_y = nx, ny
            else:
                break
        else:
            x, y = tmp_x, tmp_y
        

    return x,y