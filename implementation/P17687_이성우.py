def ten2num(x,n,letter):
    alp_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    q, r = x//n, x%n
    if r >= 10:
        r = alp_dict[r]
    letter += str(r)
    if q == 0:
        return letter[::-1]
    else:
        return ten2num(q,n,letter)
def solution(n, t, m, p):
    answer = ''
    i = 0
    while len(answer) < m*t+1:
        answer += ten2num(i,n,'')
        i += 1
    answer = answer[p-1::m][:t]
    return answer