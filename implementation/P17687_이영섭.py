rem = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def dec_to_other(num, n):
    ans = ''
    if num == 0:
        return '0'
    while num != 0:
        if num % n in rem:
            ans += rem[num % n]
        else:
            ans += str(num % n)
        num //= n
    return ans[::-1]

def solution(n, t, m, p):
    answer = ''
    whole_num = ''
    for i in range(t*m):
        whole_num += dec_to_other(i, n)
    for i in range(p-1, p+m*(t-1), m):
        answer += whole_num[i]
    return answer