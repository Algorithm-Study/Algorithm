from collections import Counter

st = input()
st_cnt = Counter(st)
st += st
ans = float('inf')
for i in range(st_cnt['a'] + st_cnt['b']):
    cnt = Counter(st[i:i+st_cnt['a']])
    ans = min(ans, cnt['b'])
print(ans)