def solution(storey):
    answer = 0
    div_num = 10
    while storey != 0:
        if storey % div_num < 5:
            answer += storey % div_num
            storey = storey // div_num
            
        elif storey % div_num == 5:
            answer += storey % div_num
            if storey // (div_num) % 10 > 4:
                storey = storey // div_num + 1
            else:
                storey = storey // div_num
                
        else:
            answer += 10 - storey % div_num
            storey = storey // div_num + 1

    
    return answer