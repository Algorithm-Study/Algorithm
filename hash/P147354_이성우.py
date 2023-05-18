def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : [x[col-1],-x[0]])
    
    for idx in range(row_begin,row_end+1):
        answer = answer^sum(i % idx for i in data[idx-1])
        
    return answer