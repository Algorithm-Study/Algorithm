def solution(rows, columns, queries):
    answer = []
    data = [[i*columns+x for x in range(1,columns+1)]for i in range(rows)]
    #print(data)
    for i in range(len(queries)):
        #for d in data:
        #    print(d)
        #print('='*30)
        min_row, min_col, max_row, max_col = [x-1 for x in queries[i]]
        horizontal = max_row- min_row
        vertical = max_col - min_col
        min_val = 10001
        #좌상단 이동
        temp = data[min_row][max_col]
        for i in range(max_col, min_col, -1):
            min_val = min(data[min_row][i-1], min_val)
            data[min_row][i] = data[min_row][i-1]
        #우상단 이둥
        temp2 = data[max_row][max_col]
        for i in range(max_row, min_row+1, -1):
            min_val = min(data[i-1][max_col], min_val)
            data[i][max_col] = data[i-1][max_col]
        min_val = min(temp, min_val)
        data[min_row+1][max_col] = temp
        #우하단 이동
        temp = data[max_row][min_col]
        for i in range(min_col, max_col):
            min_val = min(data[max_row][i+1], min_val)
            data[max_row][i] = data[max_row][i+1]
        min_val = min(temp2, min_val)
        data[max_row][max_col-1] = temp2
        #좌하단 이동
        for i in range(min_row, max_row-1):
            min_val = min(data[i+1][min_col], min_val)
            data[i][min_col] = data[i+1][min_col]
        min_val = min(temp, min_val)
        data[max_row-1][min_col] = temp
        answer.append(min_val)
    return answer