l, c = map(int, input().split())
choices = list(input().split())
choices.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
result = []
def dfs(idx, count, pwd):
    if idx >= c and count < l:
        return
    # 길이가 조건에 도달한 경우
    if count == l:
        v_count = sum([1 for x in pwd if x in vowel])
        if v_count >= 1 and l-v_count >=2:
            result.append(pwd)
        return
    # idx를 선택하는 경우
    dfs(idx+1, count+1, pwd + choices[idx])
    # idx를 선택하지 않는 경우
    dfs(idx+1, count, pwd)

dfs(0, 0, '')
result.sort()
for r in result:
    print(r)
# 조건에 맞게 정렬하여 암호를 생성
# 조건에 맞지 않는 경우 이전으로 돌아감