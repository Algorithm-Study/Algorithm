from math import sqrt
def solution(m, n, startX, startY, balls):
    answer = []
    # print(startX, startY, balls)
    corner = [[0, 0], [m, 0], [0, n], [m, n]]
    for b in balls:
        min = 10000001
        case = [[-b[0], b[1]], [b[0], -b[1]], [2*m-b[0], b[1]], [b[0], 2*n-b[1]]]
            
        for i in range(len(case)):
            if i == 0 and startY == b[1] and startX > b[0]:
                continue
            elif i == 1 and startX == b[0] and startY > b[1]:
                continue
            elif i == 2 and startY == b[1] and startX < b[0]:
                continue
            elif i == 3 and startX == b[0] and startY < b[1]:
                continue
            dist = (startX - case[i][0])**2 + (startY - case[i][1])**2
            if min > dist:
                min = dist
        for c in corner:
            if (startY - c[1])/(startX - c[0]) == (b[1] - c[1])/(b[0] - c[0]):
                dist = (startX - c[0]) ** 2 + (startY - c[1]) ** 2 + (b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2
                if min > dist:
                    min = dist
                    # print(c, b)
        answer.append(min)
    return answer