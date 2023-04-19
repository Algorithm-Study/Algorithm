N = int(input())
road = list(map(int, input().split()))
dpl = list(map(int, input().split()))
for i in range(1, len(dpl)):
    dpl[i] = min(dpl[i-1], dpl[i])
ans = 0
for idx, r in enumerate(road):
    ans += dpl[idx] * r
print(ans)

# N = int(input())
# road = list(map(int, input().split()))
# dpl = list(map(int, input().split()))
# new_dpl = []
# for idx, dp in enumerate(dpl):
#     new_dpl.append((idx, dp))
# new_dpl.sort(key= lambda x: x[1])
# ans = 0
# for idx, r in enumerate(road):
#     for nd in new_dpl:
#         if nd[0] <= idx:
#             ans += nd[1] * r
#             break
# print(ans)

# 문제 접근 방법
# # N이 10만이어서 O(N^2)은 서브태스크 3번에서 터짐
# # 각 주유소까지의 최솟값을 구해서 그 값들로 도로를 달리면 됨