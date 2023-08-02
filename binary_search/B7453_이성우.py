from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input().rstrip())

answer = 0
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for dic, num in zip([A, B, C, D], [a, b, c, d]):
        dic.append(num)
        
AB = defaultdict(int)
for a in A:
    for b in B:
        AB[a+b] += 1
        
for c in C:
    for d in D:
        cd_sum = (c+d) * -1
        if cd_sum in AB.keys():
            answer += AB[cd_sum]

print(answer)