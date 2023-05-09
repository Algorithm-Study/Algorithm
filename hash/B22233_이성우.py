import sys
input = sys.stdin.readline
# 초기 변수값
n, m = map(int, input().split())
memo = {input().rstrip() for _ in range(n)}

# 사용한 단어 집합으로 만들어서 차집합 계산
for _ in range(m):
    report = set(input().rstrip().split(','))
    # defference_update의 parameter는 Iterable이다
    # 굳이 set으로 만들지 않아도 된다
    memo.difference_update(report)
    print(len(memo))
    
# memo -= report로도 연산가능
'''
import os

s = os.read(0, os.fstat(0).st_size).split()
n = int(s[0])
keys = set(s[2 : 2 + n])
ans = []
for line in s[2 + n :]:
    keys.difference_update(line.split(b","))
    ans.append(len(keys))
print("\n".join(map(str, ans)))
# 450ms
'''
'''
N,M,*A=open(0).read().split()
N=int(N)
S={*A[:N]}
for l in A[N:]:S-={*l.split(",")};print(len(S))
'''