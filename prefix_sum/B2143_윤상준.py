import bisect
t = int(input())
n = int(input())
arrayA = list(map(int, input().split()))
m = int(input())
arrayB = list(map(int, input().split()))
# 누적합 구하기
A = []
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += arrayA[j]
        A.append(temp)
B = []
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += arrayB[j]
        B.append(temp)
B.sort()
answer = 0
for a in A:
    b = t-a
    left = bisect.bisect_left(B,b)
    if left == len(B):
        continue
    right = bisect.bisect_right(B,b)
    if B[left] == b:
        answer += right - left
print(answer)

# 배열의 모든 누적합을 찾아야 해서 분류에 누적합이 들어감
# 이후 탐색에 이분탐색 적용
# 여기서는 구현 말고 Pyhon의 bisect를 활용해서 해결