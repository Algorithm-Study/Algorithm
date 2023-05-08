# 조합 등을 활용해서 모든 경우의 수를 구하는 것은 불가능
# 규칙을 찾아야 함 -> 최대한 균등하게 나눠야 곱했을 때 가장 큰 값이 됨
def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    for i in range(n,0,-1):
        answer.append(s//i)
        s = s - s//i
    return answer