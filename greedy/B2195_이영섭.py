S = input()
P = input()
ans = 0
idx_s, idx_e = 0, 0

while idx_s < len(P):
    for i in range(len(S) - (idx_e - idx_s)):
        if S[i:i + (idx_e - idx_s) + 1] == P[idx_s:idx_e + 1]:
            idx_e += 1
            break
    else:
        ans += 1
        idx_s = idx_e
        idx_e = idx_s
print(ans)