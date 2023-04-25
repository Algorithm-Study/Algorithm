T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
idA, idB = 0, 0
dictA, dictB = {}, {}
for i in range(n):
    sumA = A[i]
    if sumA in dictA:
        dictA[sumA] += 1
    else:
        dictA[sumA] = 1
    for j in range(i+1, n):
        sumA += A[j]
        if sumA in dictA:
            dictA[sumA] += 1
        else:
            dictA[sumA] = 1

for i in range(m):
    sumB = B[i]
    if sumB in dictB:
        dictB[sumB] += 1
    else:
        dictB[sumB] = 1
    for j in range(i + 1, m):
        sumB += B[j]
        if sumB in dictB:
            dictB[sumB] += 1
        else:
            dictB[sumB] = 1

ans = 0
for Akey in dictA.keys():
    if T - Akey in dictB:
        ans += dictA[Akey] * dictB[T - Akey]
print(ans)

# 문제 접근 방법
# # prefix_sum으로 어떻게 푸는지 모르겠다.
# # A, B의 부분집합을 모두 구해준 후, dict를 이용하여 값을 구함
# # N = 1000이라 가능했던 해결 방법