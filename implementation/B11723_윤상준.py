import sys
input = sys.stdin.readline
n = int(input())
data = set()
for _ in range(n):
    op = input().split()
    if len(op) == 1:
        if op[0] == 'all':
            data = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        else:
            data = set()
    if op[0] == 'add':
        data.add(int(op[1]))
    elif op[0] == 'remove':
        data.discard(int(op[1]))
    elif op[0] == 'check':
        if int(op[1]) in data:
            print(1)
        else:
            print(0)
    elif op[0] == 'toggle':
        if int(op[1]) in data:
            data.discard(int(op[1]))
        else:
            data.add(int(op[1]))