# t*m 길이인 문자열이 될 때까지 진행한 다음 m 간격으로 뽑으면 해결
from collections import deque
intto = ['0', '1', '2', '3','4','5','6','7','8','9','A', 'B', 'C','D','E','F']
def solution(n, t, m, p):
    val = 0
    sequence = ['0']
    while True:
        queue = []
        temp = val
        while temp != 0:
            queue.append(intto[temp%n])
            temp = temp // n
        sequence.extend(queue[::-1])
        val += 1
        if len(sequence) >= t*m:
            break
    answer = sequence[p-1::m]
    return ''.join(answer[:t])