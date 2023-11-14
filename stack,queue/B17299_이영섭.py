from collections import Counter

N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

ans = [-1] * N
st = [0]

for i in range(1, N):
    while st and counter[A[st[-1]]] < counter[A[i]]:
        ans[st.pop()] = A[i]
    st.append(i)

print(*ans)