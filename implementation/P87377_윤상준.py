def solution(line):
    INF = float('inf')
    xmin, ymin = INF, INF
    xmax, ymax = -INF, -INF
    points = []
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            a,b,e =line[i]
            c,d,f = line[j]
            if a*d != b*c:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x == int(x) and y == int(y):
                    xmin, xmax = min(xmin,int(x)), max(xmax, int(x))
                    ymin, ymax = min(ymin,int(y)), max(ymax,int(y))
                    points.append([int(x),int(y)])
    answer = ['.' * (xmax - xmin + 1)] * (ymax-ymin+1)
    for point in points:
        x, y = point
        answer[ymax-y] = answer[ymax-y][:x-xmin] + '*' + answer[ymax-y][x-xmin+1:]
    return answer
# 좌표가 뒤집힌 형태인 것과 입력 값의 범위에 주의해야 함!