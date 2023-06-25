def manachers(S, N):
    A = [0] * N
    r, p = 0, 0
    for i in range(N):
        if i <= r:
            A[i] = min(A[2 * p - i], r - i)
        while i - A[i] - 1 >= 0 and i + A[i] + 1 < N and S[i - A[i] - 1] == S[i + A[i] + 1]:
            A[i] += 1
        if r < i + A[i]:
            r = i + A[i]
            p = i
    return A
def solution(s):
    S = "#"+"#".join(list(s))+"#"
    return max(manachers(S, len(S)))

# O(n)을 보장하는 Manacher 알고리즘을 활용하면 매우 빠르게 문제해결 가능
# A[i]: i를 기준으로 회문을 만족하는 최대 길이(반지름)
# r 회문을 만족하는 최대 위치
# 최대 회문을 만족하는 i의 위치
# #을 추가한 이유는 해당 알고리즘의 경우 홀수 회문만 검출할 수 있기 때문에 짝수 회문에 대응하려면 #을 추가해야 함