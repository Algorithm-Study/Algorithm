def solution(x, y, n):
    count_list = [9999999]*(y+1)
    count_list[x] = 0
    answer = -1
    for i in range(1,y+1):
        if count_list[i] == 9999999:
            continue
        if i + n <= y:
            count_list[i+n] = count_list[i]+1 if count_list[i] < count_list[i+n] else count_list[i+n]
        if i * 2 <= y:
            count_list[i*2] = count_list[i]+1 if count_list[i] < count_list[i*2] else count_list[i*2]
        if i * 3 <= y:
            count_list[i*3] = count_list[i]+1 if count_list[i] < count_list[i*3] else count_list[i*3]
        #print(count_list)
    if count_list[y] != 9999999:
        return count_list[y]
    
    return answer