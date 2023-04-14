def solution(k, ranges):
    answer = []
    ubak = [k]
    while k != 1:
        if k % 2 == 0:
            k /= 2
        else:
            k = 3*k + 1
        ubak.append(k)
    # print(ubak)

    area = []
    for i in range(1,len(ubak)):
        area.append((ubak[i-1]+ubak[i])/2)
    # print(area)
    num = len(area)
    for i,j in ranges:
        if i > num+j:
            answer.append(-1)
        else:
            answer.append(sum(area[i:num+j]))

    return answer