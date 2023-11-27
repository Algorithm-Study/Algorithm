from collections import defaultdict

S, P = map(int, input().split())
word = list(input())
A, C, G, T = map(int, input().split())
ans = 0
ct = defaultdict(int)
for i in range(P):
    if word[i] == 'A':
        ct['A'] += 1
    elif word[i] == 'C':
        ct['C'] += 1
    elif word[i] == 'G':
        ct['G'] += 1
    elif word[i] == 'T':
        ct['T'] += 1
if ct['A'] >= A and ct['C'] >= C and ct['G'] >= G and ct['T'] >= T:
    ans += 1

for i in range(P, S):
    ct[word[i-P]] -= 1
    ct[word[i]] += 1
    if ct['A'] >= A and ct['C'] >= C and ct['G'] >= G and ct['T'] >= T:
        ans += 1
print(ans)
