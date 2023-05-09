import sys
input = sys.stdin.readline
n, m = map(int, input().split())
keyword = {}
for _ in range(n):
    keyword[input().rstrip()] = 1
posted = []
for _ in range(m):
    temp = list(map(str, input().rstrip().split(',')))
    for t in temp:
        if keyword.get(t, 0):
            keyword[t] -= 1
            n -= 1
    print(n)

# pypy 및 sys 미사용시 문제 통과 불가능
# dict의 get 매서드를 활용해서 문제해결
# get(x, value) -> key x가 존재하지 않는 경우 0 return