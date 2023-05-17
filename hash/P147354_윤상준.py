def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col-1], -x[0]))
    mod_result = []
    for i in range(row_begin-1,row_end):
        temp = 0
        for d in data[i]:
            temp += d % (i+1)
        mod_result.append(temp)
    temp = mod_result[0]
    for mod in mod_result[1:]:
        temp = temp ^ mod
    return temp