def solution(park, routes):
    answer = []
    row = len(park)
    column = len(park[0])
    for idx,p in enumerate(park):
        if 'S' in p:
            start = [idx, p.index('S')]
    for route in routes:
        way, count = route.split()
        count = int(count)
        if way == 'E':
            if start[1] + count >= column:
                continue
            if 'X' in park[start[0]][start[1]: (start[1] + count+1)]:
                continue
            start[1] += count
        if way == 'W':
            if start[1] - count < 0:
                continue
            if 'X' in park[start[0]][start[1] - count:start[1] + 1]:
                continue
            start[1] -= count
        if way == 'N':
            if start[0] - count < 0:
                continue
            if 'X' in [park[x][start[1]] for x in range(start[0]-count, start[0]+1) ]:
                continue
            start[0] -= count
        if way == 'S':
            if start[0] + count >= row:
                continue
            if 'X' in [park[x][start[1]] for x in range(start[0], start[0]+count+1) ]:
                continue
            start[0] += count
    answer = start
    return answer