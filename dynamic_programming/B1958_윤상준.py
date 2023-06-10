A = [0] + list(input())
B = [0] + list(input())
C = [0] + list(input())
LCS = [[[0]*len(C) for _ in range(len(B))] for _ in range(len(A))]

for i in range(1, len(A)):
    for j in range(1, len(B)):
        for k in range(1, len(C)):
            if A[i] == B[j] and B[j] == C[k]:
                LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
            else:
                LCS[i][j][k] = max(LCS[i-1][j][k], LCS[i][j-1][k], LCS[i][j][k-1])
result = LCS[-1][-1][-1]
print(result)

# LCS를 3개 단어를 기준으로 구해야 함
# 3차원 DP 생성해서 진행하는 문제