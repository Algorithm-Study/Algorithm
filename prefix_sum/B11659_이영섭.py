import sys
input = sys.stdin.readline

# 4번 제출
N, M = map(int, input().split())
N_list = list(map(int, input().split()))

# 1번 제출
for _ in range(M):
    ans = 0
    i, j = map(int, input().split())
    for idx in range(j - i + 1):
        ans += N_list[i-1+idx]
    print(ans)

# 2번 제출
for _ in range(M):
    i, j = map(int, input().split())
    print(sum(N_list[i-1:j]))
    
# 3번 제출
prefix_sum = [0]

temp = 0
for tmp in N_list:
    temp += tmp
    prefix_sum.append(temp)  
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
    
# 문제 접근 방법
# # 간단한 구현 문제인줄 알았으나 시간초과의 이슈로 누적 합이라는 새로운 알고리즘 접근 법을 배움
# 새로 배운 python
# # input = sys.stdin.readline을 하게 되면 input이 sys.stdin.readline의 속도를 가짐
# # input은 프롬프트 입력을 받을 수 있지만 stdin은 그렇지 못함
# # stdin은 개행문자('\n')까지 입력으로 받기 때문에 rstrip()이나 split()을 활용해 제거