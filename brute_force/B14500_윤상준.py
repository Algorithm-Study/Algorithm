# 메모리: 131312KB, 시간: 808ms
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().rstrip().split())))
max_val = 0
#print(data)
# 1X4 케이스
for i in range(n):
    cases = [sum(data[i][x:x+4]) for x in range(m-3)]
    for case in cases:
        if case > max_val:
            max_val = case
# 4X1 케이스
for i in range(n-3):
    cases = [data[i][x] + data[i+1][x] + data[i+2][x] + data[i+3][x] for x in range(m)]
    for case in cases:
        if case > max_val:
            max_val = case
# 2X2 케이스
for i in range(n-1):
    cases = [sum(data[i][x:x+2]) + sum(data[i+1][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
# 3X2 케이스
for i in range(n-2):
    cases = [data[i][x] + data[i+1][x] + sum(data[i+2][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i][x] + data[i+2][x+1] + sum(data[i+1][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i][x+1] + data[i+1][x+1] + sum(data[i+2][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i][x+1] + data[i+2][x] + sum(data[i+1][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i][x] + data[i+2][x] + sum(data[i+1][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i][x+1] + data[i+2][x+1] + sum(data[i+1][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i+2][x] + data[i+1][x] + sum(data[i][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-2):
    cases = [data[i+2][x+1] + data[i+1][x+1] + sum(data[i][x:x+2]) for x in range(m-1)]
    for case in cases:
        if case > max_val:
            max_val = case
# 2X3 케이스
for i in range(n-1):
    cases = [sum(data[i][x:x+3]) + data[i+1][x+1] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i+1][x:x+3]) + data[i][x+1] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i][x:x+3]) + data[i+1][x+2] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i+1][x:x+3]) + data[i][x+2] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i+1][x:x+3]) + data[i][x] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i][x:x+3]) + data[i+1][x] for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i][x:x+2]) + sum(data[i+1][x+1:x+3]) for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
for i in range(n-1):
    cases = [sum(data[i+1][x:x+2]) + sum(data[i][x+1:x+3]) for x in range(m-2)]
    for case in cases:
        if case > max_val:
            max_val = case
print(max_val)