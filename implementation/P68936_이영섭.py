def check_val(S, n):
    if n == 1:
        answer[S[0][0]] += 1
        return
    sum_val = sum([sum(S[i]) for i in range(n)])
    if sum_val == n**2:
        answer[1] += 1
        return
    if sum_val == 0:
        answer[0] += 1
        return
    check_val([[S[i][j] for j in range(n//2)] for i in range(n//2)], n//2)
    check_val([[S[i][j] for j in range(n//2, n)] for i in range(n//2)], n//2)
    check_val([[S[i][j] for j in range(n//2)] for i in range(n//2, n)], n//2)
    check_val([[S[i][j] for j in range(n//2, n)] for i in range(n//2, n)], n//2)
    return 0

def solution(arr):
    global answer
    answer = [0, 0]
    check_val(arr, len(arr))
    return answer