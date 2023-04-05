# stack으로 풀면 더 쉽게 해결 가능
def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    for idx, plan in enumerate(plans):
        start_h, start_m = map(int,plan[1].split(':'))
        if idx == len(plans) - 1:
            answer.append(plan[0])
            plan[2] = str(0)
            break
        next_h, next_m = map(int,plans[idx+1][1].split(':'))
        time_limit = (next_h - start_h) * 60 + (next_m - start_m)
        if time_limit == int(plan[2]):
            answer.append(plan[0])
            plan[2] = str(0)
        elif time_limit > int(plan[2]):
            answer.append(plan[0])
            time_limit -= int(plan[2])
            plan[2] = str(0)
            for back in range(idx, -1, -1):
                print(plans[back])
                if int(plans[back][2]) != 0:
                    if time_limit < int(plans[back][2]):
                        plans[back][2] = str(int(plans[back][2]) - time_limit)
                        break
                    elif time_limit == int(plans[back][2]):
                        plans[back][2] = str(0)
                        answer.append(plans[back][0])
                        break
                    else:
                        answer.append(plans[back][0])
                        time_limit -= int(plans[back][2])
                        plans[back][2] = str(0)
        else:
            plan[2] = str(int(plan[2]) - time_limit)
    plans = plans[::-1]
    for i in range(len(plans)):
        if int(plans[i][2]) > 0:
            answer.append(plans[i][0])
    
    return answer