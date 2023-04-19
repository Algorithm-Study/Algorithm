import sys
input = sys.stdin.readline
n, m = map(int, input().split())
memo = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word not in memo:
            memo[word] = 1
        else:
            memo[word] += 1
            
answer = sorted(memo.items(), key = lambda x : [-x[1], -len(x[0]), x[0]])

for v, k in answer:
    print(v)

# readline 안해서 시간초과
# from 19:57 to 20:11