def solution(rows, columns, queries):
    maps = [[(x-1)*columns+y for y in range(1,columns+1)] for x in range(1,rows+1)]
    answer = []
    
    for query in queries:
        temp = []
        x1, y1, x2, y2 = query
        key = maps[x1-1][y2-1]
        temp.append(key)
        maps[x1-1][y1:y2] = maps[x1-1][y1-1:y2-1]
        temp += maps[x1-1][y1:y2]
        for i in range(x1-1,x2-1):
            maps[i][y1-1] = maps[i+1][y1-1]
            temp.append(maps[i][y1-1])
        maps[x2-1][y1-1:y2-1] = maps[x2-1][y1:y2]
        temp += maps[x2-1][y1-1:y2-1]
        for i in range(x2-1,x1,-1):
            maps[i][y2-1] = maps[i-1][y2-1]
            temp.append(maps[i][y2-1])

        maps[x1][y2-1] = key
        answer.append(min(temp))
        
    # print(maps)

    return answer