from itertools import product
import sys
input = sys.stdin.readline

# def cal_num(button, num):
#     if num not in button:
#         return [str(num)]
#     dif = 10
#     ret = []
#     for i in range(11):
#         if i not in button and abs(num - i) < dif:
#             dif = num - i
#             ret = [str(i)]
#         elif i not in button and abs(num - i) == dif:
#             ret.append(str(i))
#     return ret

# def dfs(ls, temp, cnt, n):
#     if cnt == n:
#         ans.append(temp)
#         return
#     for i in ls[cnt]:
#         temp += i
#         dfs(ls, temp, cnt+1, n)
#         temp = temp[:-1]

# ans = []
# N = input().rstrip()
# M = int(input().rstrip())
# if M == 0:
#     print(len(N))
# else:
#     button = list(map(int, input().rstrip().split()))

#     ls = []
#     for i in range(len(N)):
#         ls.append(cal_num(button, int(N[i])))
#     dfs(ls, "", 0, len(N))
#     print(ans)
#     diff = 1000000
#     diff_100 = 1000000
#     for answer in ans:
#         if abs(int(answer) - int(N)) < diff:
#             diff = abs(int(answer) - int(N))
#         if abs(int(N) - 100) < diff_100:
#             diff_100 = abs(int(N) - 100)
#     print(min(diff + len(N), diff_100))
bt_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
N = input().rstrip()
M = int(input().rstrip())
if M == 0:
    print(min(len(N), abs(int(N) - 100)))
elif M == 10:
    print(abs(int(N) - 100))
else:
    button = list(input().rstrip().split())
    bt_list = [x for x in bt_list if x not in button]
    bf = list(product(bt_list, repeat = len(N)))
    bf += list(product(bt_list, repeat = len(N)-1))
    bf += list(product(bt_list, repeat = len(N)+1))
    diff_100 = abs(int(N) - 100)
    diff = 1000000
    ans = 0
    for ks in bf:
        if len(ks) > 1 and diff > abs(int(''.join(ks)) - int(N)) + len(ks):
            diff = abs(int(''.join(ks)) - int(N)) + len(ks)
            if ks[0] == '0':
                diff -= 1
        elif len(ks) == 1 and diff > abs(int(ks[0]) - int(N)) + len(ks):
            diff = abs(int(ks[0]) - int(N)) + len(ks)
    print(min(diff, diff_100))

# 문제 접근 방법
# # 각 자리마다 가장 가까운 숫자를 선택해서 조합한 다음 계산하려 함
# # 자리수가 다를 때의 방법을 생각할 수 없었음
# # 최대 10^6이기 때문에 중복 순열로 모든 경우를 살펴봐도 시간 내에 가능하여 완탐으로 변경
# # product를 사용하여 자리수-1, 자리수, 자리수+1 모든 경우를 살펴봄
# # 한자리 수인 경우, 고장이 안난 경우, 전부 고장난 경우에 대해서는 예외 처리를 해줌