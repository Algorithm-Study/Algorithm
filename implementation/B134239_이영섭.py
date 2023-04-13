def solution(k, ranges):
    answer = []
    ubak = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        ubak.append(k)
    for rg in ranges:
        val = 0
        if rg[0] > len(ubak) + rg[1] - 1:
            answer.append(-1)
            continue
        else:
            left = rg[0]
            right = len(ubak) + rg[1] - 1
        
        for idx in range(left, right):
            val += (ubak[idx] + ubak[idx+1])/2
        answer.append(val)
    return answer