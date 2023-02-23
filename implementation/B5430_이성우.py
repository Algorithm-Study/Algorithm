import sys
from collections import deque

number_of_case = int(sys.stdin.readline().rstrip())

for i in range(number_of_case):
    func_list = sys.stdin.readline().rstrip()
    problem_len = int(sys.stdin.readline().rstrip())
    problem = sys.stdin.readline().rstrip()[1:-1].split(',')
    reverse_TF = False
    if problem != ['']:
        problem = deque(problem)
    else:
        problem = []

    for func_char in func_list:
        if func_char == 'R':
            if reverse_TF == False:
                reverse_TF = True
            else:
                reverse_TF = False

        if func_char == 'D':
            if len(problem) != 0:
                if reverse_TF == False:
                    problem.popleft()
                else:
                    problem.pop()
            else:
                print('error')
                break
    else:
        if reverse_TF == True:
            problem.reverse()
        print('[' + ','.join(problem) +']')