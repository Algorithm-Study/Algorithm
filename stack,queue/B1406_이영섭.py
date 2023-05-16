import sys
input = sys.stdin.readline

c_left = list(input().rstrip())
c_right = []

M = int(input())
for _ in range(M):
    com = input()
    if com[0] == 'L' and c_left:
        c_right.append(c_left.pop())
    elif com[0] == 'D' and c_right:
        c_left.append(c_right.pop())
    elif com[0] == 'B' and c_left:
        c_left.pop()
    elif com[0] == 'P':
        c_left.append(com[2])

print(''.join(c_left) + ''.join(c_right[::-1]))