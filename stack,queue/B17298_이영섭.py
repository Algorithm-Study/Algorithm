from collections import deque

N = int(input())
data = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
st, idx = deque(), deque()
for iid, i in enumerate(data):
    while st and st[-1] < i:
        ths = st.pop()
        ans[idx[-1]] = i
        idx.pop()
    st.append(i)
    idx.append(iid)

for i in range(N):
    print(ans[i], end=" ")