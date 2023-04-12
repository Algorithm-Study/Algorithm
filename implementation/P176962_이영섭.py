from collections import deque

def solution(plans):
    answer = []
    for i in range(len(plans)):
        time = plans[i][1].split(":")
        plans[i].append(int(time[0])*60 + int(time[1]))
    plans.sort(key= lambda x:x[3])
    # print(plans)
    time = plans[0][3] + int(plans[0][2])
    temp = []
    for i in range(1, len(plans)):
        # print(time, plans[i][3])
        if time > plans[i][3]:
            temp.append([plans[i-1][0], time - plans[i][3]])
        elif time == plans[i][3]:
            answer.append(plans[i-1][0])
        else:
            answer.append(plans[i-1][0])
            while temp:
                last = temp.pop()
                if plans[i][3] > time + last[1]:
                    time += last[1]
                    answer.append(last[0])
                elif plans[i][3] == time + last[1]:
                    answer.append(last[0])
                    break
                else:
                    temp.append([last[0], time + last[1] - plans[i][3]])
                    break
        time = plans[i][3] + int(plans[i][2])
        # print(temp, time)
    answer.append(plans[-1][0])
    while temp:
        last = temp.pop()
        answer.append(last[0])
    # print(temp)
    return answer