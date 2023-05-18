def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key= lambda x:(x[col-1], -x[0]))
    s_i_list = []
    for i, dt in enumerate(data):
        s_i = 0
        for col in dt:
            s_i += col % (i+1)
        s_i_list.append(s_i)
    for i in range(row_begin-1, row_end):
        answer = answer ^ s_i_list[i]
    return answer