from itertools import combinations
def solution(line: list) -> list:
    answer = []
    tmp = set()
    for lines in combinations(line, 2):
        line1, line2 = lines
        A, B, E = line1
        C, D, F = line2
        if A*D - B*C != 0:
            x = (B*F - E*D)/(A*D - B*C)
            y = (E*C - A*F)/(A*D - B*C)
            if x == int(x) and y == int(y):
                tmp.add((int(x),int(y)))
                
    x_min = y_min = float('inf')
    x_max = y_max = (-1)*float('inf')

    for x, y in tmp:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    arr = [['.' for _ in range((x_max-x_min+1))] for _ in range(y_max-y_min+1)]
    
    for x, y in tmp:
        arr[y_max - y][x - x_min] = '*'
    
    for tmp in arr:
        answer.append(''.join(tmp))
    return answer