def solution(park, routes):
    answer = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                point = [i, j]
    for route in routes:
        command = route.split()
        if command[0] == 'E':
            for np in range(point[1], point[1]+int(command[1])+1):
                if np < 0 or np >= len(park[0]):
                    break
                if park[point[0]][np] == 'X':
                    break
            else:
                point[1] += int(command[1])
        elif command[0] == 'W':
            for np in range(point[1], point[1]-int(command[1])-1, -1):
                if np < 0 or np >= len(park[0]):
                    break
                if park[point[0]][np] == 'X':
                    break
            else:
                point[1] -= int(command[1])
        elif command[0] == 'S':
            for np in range(point[0], point[0]+int(command[1])+1):
                if np < 0 or np >= len(park):
                    break
                if park[np][point[1]] == 'X':
                    break
            else:
                point[0] += int(command[1])
        else:
            for np in range(point[0], point[0]-int(command[1])-1, -1):
                if np < 0 or np >= len(park):
                    break
                if park[np][point[1]] == 'X':
                    break
            else:
                point[0] -= int(command[1])
    answer = point
    return answer