def solution(n, s):
    answer = []
    sum_val = 1
    if n > s:
        return [-1]
    else:
        div = s // n
        answer = [div for _ in range(n)]
        rem = s % n
        for i in range(rem):
            answer[i] += 1
    answer.sort()
        
    return answer

# 문제 접근 방법
# # 곱이 가장 크려면 최대한 비슷한 숫자로 집합을 구성해야 함
# # 이 난이도가 레벨3..?