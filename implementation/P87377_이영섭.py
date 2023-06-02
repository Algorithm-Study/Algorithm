def solution(line):
    answer = []
    dot = set()
    for i in range(len(line)):
        for j in range(len(line)):
            if i == j:
                continue
            
            A, B, E = line[i][0], line[i][1], line[i][2]
            C, D, F = line[j][0], line[j][1], line[j][2]
            
            if A*D == B*C:
                continue
                
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            
            if float.is_integer(x) and float.is_integer(y):
                dot.add((int(x), int(y)))
    minx, maxx = min([x for x, y in dot]), max([x for x, y in dot])
    miny, maxy = min([y for x, y in dot]), max([y for x, y in dot])
    for i in range(maxy, miny-1, -1):
        temp = ''
        for j in range(minx, maxx+1):
            if (j, i) in dot:
                temp += '*'
            else:
                temp += '.'
        answer.append(temp)
    return answer