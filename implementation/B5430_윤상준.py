#deque 안 써도 시간 초과 안 걸림 다만 reverse 함수 사용 시 시간 초과 발생
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    operation = list(str(input().rstrip()))
    n = int(input().rstrip())
    data = [x for x in list(input().rstrip()[1:-1].split(',')) if x != '']
    if operation.count('D') > n:
        print('error')
        continue
    count = 0
    for op in operation:
        if op == 'R':
            count += 1
        else:
            if count %2 == 1:
                data.pop(-1)
            else:
                data.pop(0)
    if count %2 == 1:
        data.reverse()
    print("[" + ",".join(data) + "]")