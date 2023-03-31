import sys
input = sys.stdin.readline
from collections import deque

dc = {}
M = int(input())
for _ in range(M):
    comm = input().rstrip()
    if ' ' in comm:
        comm, num = comm.split()
        num = int(num)

    if comm == 'add':
        dc[num] = 1
    elif comm == 'remove':
        dc[num] = 0
    elif comm == 'check':
        if num in dc and dc[num] == 1:
            print(1)
        else:
            print(0)
    elif comm == 'toggle':
        if num in dc:
            dc[num] = 0
        else:
            dc[num] = 1
    elif comm == 'all':
        dc = {n: 1 for n in range(1, 21)}
    elif comm == 'empty':
        dc.clear()
# 새로 배운 python
# # sys.stdin.readline은 개행문자(\n)를 같이 입력 받으므로 rstrip을 활용해서 개행 문자를 제거해야 한다.