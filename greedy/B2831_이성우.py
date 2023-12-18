from bisect import bisect_left

# 초기값 설정
n = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))
men.sort()
women.sort()
answer = 0

def solution(plus, minus):
    global answer
    plus_idx = len(plus) - 1
    minus_idx = 0
    # 두 수의 합이 음수면서 차이가 가장 크게하여 짝을 찾아준다
    while 0 <= plus_idx and minus_idx < len(minus):
        if plus[plus_idx] + minus[minus_idx] < 0:
            answer += 1
            plus_idx -= 1
            minus_idx += 1
        else:
            plus_idx -= 1

men_zero = bisect_left(men, 0)
women_zero = bisect_left(women, 0)

# 음수와 양수가 짝지어질 수 있도록 만든다
solution(men[men_zero:], women[:women_zero])
solution(women[women_zero:], men[:men_zero])

print(answer)