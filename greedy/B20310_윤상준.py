n = input()
data = list(n)
one, zero = data.count('1'), data.count('0')
one = one//2
zero = zero//2
for _ in range(one):
    data.pop(data.index('1'))
for _ in range(zero):
    temp = data[::-1].index('0')
    data.pop(len(data)- temp - 1)
print(''.join(data))
# 재구성이 아니라 원래 순서에서 제거했을 때 사전 순으로 빠른 것을 구해야 함