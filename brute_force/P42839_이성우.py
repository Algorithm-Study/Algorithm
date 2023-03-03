from itertools import permutations as pmt
def solution(numbers):
    tmp =[]
    # 가능한 수 탐색
    for i in range(len(numbers)):
        tmp += list(set(pmt(numbers,i+1)))
    tmp2 = [int(''.join(i)) for i in tmp]
    # 소수 판별
    cnt = 0    
    for j in set(tmp2):
        if j > 1:
            for k in range(2,int(j**0.5)+1):
                if j%k == 0:
                    break
            else:
                cnt +=1
    return cnt