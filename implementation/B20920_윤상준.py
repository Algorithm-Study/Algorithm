n, m = map(int, input().split())
memorize = {}
for _ in range(n):
    word = input()
    if len(word) >= m:
        if word in memorize:
            memorize[word] += 1
        else:
            memorize[word] = 1
s_memorize = sorted(memorize.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for m in s_memorize:
    print(m[0])