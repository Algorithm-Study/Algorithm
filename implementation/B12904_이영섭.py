from collections import deque

S, T = input(), input()
str_list = deque([T])

while str_list:
    now_str = str_list.popleft()
    if now_str == S:
        print(1)
        exit()
    if len(now_str) < len(S):
        print(0)
        exit()

    if now_str[-1] == 'A':
        str_list.append(now_str[:-1])
    else:
        str_list.append(now_str[:-1][::-1])
print(0)
