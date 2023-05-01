N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]

inc_len = [1]*N
dec_len = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            inc_len[i] = max(inc_len[i], inc_len[j] + 1)
        if reverse_A[i] > reverse_A[j]:
            dec_len[i] = max(dec_len[i], dec_len[j] + 1)

result = [inc_len[i] + dec_len[N-i-1] - 1 for i in range(N)]
print(max(result))

# 문제 접근 방법
# # LIS를 앞에서 한 번, 뒤에서 한 번 적용하여 둘의 합이 가장 큰 idx 값을 구함