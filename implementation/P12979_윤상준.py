def solution(n, stations, w):
    answer = 0
    no_station = []
    if len(stations) == 1:
        area = stations[0] - w - 1
        no_station.append(area)
        area = n - stations[0] - w
        no_station.append(area)
        area = 0
    else:
        for i in range(len(stations)-1):
            if i == 0 and stations[i] != 1:
                area = stations[i] - w - 1
                if area >0:
                    no_station.append(area)
            area = stations[i+1] - stations[i] - (2*w) -1
            if area > 0:
                no_station.append(area)
    if stations[-1] != n and len(stations) != 1:
        area = n - stations[-1] - w
        if area>0:
            no_station.append(area)
    for size in no_station:
        power = 2*w+1
        if size%power !=0:
            answer += size//power+1
        else:
            answer += size//power

    return answer
# Station을 기준으로 왼쪽에 몇개를 설치하는지 계산
# 오른쪽에 설치되지 않은 영역이 있으면 마지막에 계산해서 추가하면 되는 문제