# 일의 자리 수부터 시작해서 5보다 큰 경우 더하기 아닌 경우는 빼기
def solution(storey):
    count = 0
    max_c = len(str(storey)) + 1
    c = 1
    while storey != 0:
        pos = storey % (10**c)
        print(pos)
        if pos > (10**c/2):
            count += 10 - (pos // 10**(c-1))
            storey += 10**(c) - pos
        elif pos == (10**c/2) and storey% (10**(c+1))%10**c == 5:
            count += 10 - (pos // 10**(c-1))
            storey += 10**(c) - pos
        else:
            count += pos // 10**(c-1)
            storey -= pos
        c += 1
        #print(count)
    return count
#Test Case
#Input: 1555, Answer: 15
#Input: 5111, Answer: 8
#Input: 55, Answer: 10