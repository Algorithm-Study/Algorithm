import sys

input = sys.stdin.readline
s = set()
all_set = set(map(str,range(1,21)))

def add(s, x):
    s.add(x)
    return s

def remove(s, x):
    if x in s:
        s.remove(x)
    return s
        
def check(s, x):
    if x in s:
        sys.stdout.write('1\n')
    else: sys.stdout.write('0\n')
    return s

def toggle(s, x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)
    return s

def all(s, x):
    s = all_set
    return s

def empty(s, x):
    s = set()
    return s
    
solutions = {'add':add,
            'remove':remove,
            'check':check,
            'toggle':toggle,
            'all':all,
            'empty':empty
        }

for _ in range(int(input())):
    command = list(input().split())
    s = solutions[command[0]](s,command[-1])

# print() 대신에 sys.stdout.write() 을 쓰면 10% 정도 향상될 수 있다
# 문자열로 비교할 때는 set(map(str,range(1,21)))을 계속 생성하면 시간 초과가 떴다
# 하지마 미리 만들어 놓고 할당하면 시간 초과를 피할 수 있었다
# dict로 함수 불러올 수 있는 것도 상기하기

# 함수가 아니고 조건문으로 풀고 int값으로 비교하기

'''
import sys
s =set()
input = sys.stdin.readline
all_set = set(range(1,21))
empty_set = set()
for _ in range(int(input())):

    cmd = input().split()
    if 'add' in cmd:
        s.add(int(cmd[1]))
    elif 'remove' in cmd:
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
    elif 'check' in cmd:
        if int(cmd[1]) in s:
            sys.stdout.write('1\n')
        else: sys.stdout.write('0\n')
    elif 'toggle' in cmd:
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else: s.add(int(cmd[1]))
    elif 'all' in cmd:
        s = all_set
    elif 'empty' in cmd:
        s = empty_set
'''

# x 입력이 1~20까지라 미리 공간을 만들어 놓고 풀수도 있다
'''
import sys

input = sys.stdin.readline
all_set = [1 for _ in range(21)]
zero_set = [0 for _ in range(21)]
s = [0 for _ in range(21)]

for _ in range(int(input())):
    cmd = input().split()
    if 'add' in cmd:
        s[int(cmd[1])] = 1
    elif 'remove' in cmd:
        s[int(cmd[1])] = 0
    elif 'check' in cmd:
        sys.stdout.write(str(s[int(cmd[1])])+'\n')
    elif 'toggle' in cmd:
        s[int(cmd[1])] = 0 if s[int(cmd[1])] == 1 else 1
    elif 'all' in cmd:
        s = all_set
    elif 'empty' in cmd:
        s = zero_set
'''
