def dfs(cnt, idx):
    if cnt == L:
        vowel, cons = 0, 0
        for i in range(L):
            if ans[i] in vowels:
                vowel += 1
            else:
                cons += 1
        if vowel >= 1 and cons >= 2:
            print("".join(ans))
        return
    for i in range(idx, C):
        ans.append(alphabet[i])
        dfs(cnt + 1, i + 1)
        ans.pop()


L, C = map(int, input().split())
alphabet = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
alphabet.sort()
ans = []
dfs(0, 0)
