S = input()
T = input()

def dfs(S, T):
    retA, retB = False, False
    if len(S) == len(T):
        if S != T:
            return False
        else:
            return True
    if T[-1] == 'A':
        retA = dfs(S, T[:-1])
    if T[0] == 'B':
        T = T[::-1]
        retB = dfs(S, T[:-1])
    return retA or retB
if dfs(S, T) == True:
    print(1)
else:
    print(0)

# 문제 접근 방법
# # S를 T로 늘리면 모든 경우의 수가 2^(len(T)-len(S))이므로 시간초과
# # T를 S로 줄이면 맨 앞이 B일 때만 줄일 수 있고, 맨 뒤가 A일 때만 T를 줄일 수 있다.

# def add_A(string):
#     string += 'A'
#     return string

# def add_B(string):
#     string += 'B'
#     return string[::-1]

# def product(arr, r):
#     for i in range(len(arr)):
#         if r == 1: yield [arr[i]]
#         else:
#             for next in product(arr, r-1):
#                 yield [arr[i]] + next

# def solution():
#     str = S
#     case = [add_A, add_B]
#     bf = list(product(case, len(T)-len(S)))
#     for cs in bf:
#         str = S
#         for func in cs:
#             str = func(str)
#         if str == T:
#             return 1
#     return 0

# print(solution())