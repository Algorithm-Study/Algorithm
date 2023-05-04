def solution(dirs):
    
    point = {}
    x, y = 0, 0
    for i in list(dirs):
        cx, cy = x, y
        nx, ny = x, y
        if i == 'L':
            nx = x - 1
        elif i == 'R':
            nx = x + 1
        elif i == 'U':
            ny = y + 1
        else:
            ny = y - 1
        temp = [(cx, cy), (nx, ny)]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            temp.sort()
            point[tuple(temp)] = 1
            x, y = nx, ny
    return len(point)

# 문제 접근 방법
# # 출발 좌표와 도착 좌표를 정렬해서 dict에 넣어주면 간단하게 선분을 기록할 수 있다.