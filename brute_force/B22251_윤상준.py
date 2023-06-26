display = [0b1111110, 0b0110000, 0b1101101, 0b1111001, 0b0110011, 0b1011011, 0b1011111, 0b1110000, 0b1111111, 0b1111011]
n, k, P, x = map(int, input().split())
x2digit = '0'*(k-len(str(x))) + str(x)
cases = []
def dfs(x2digit, idx, p, after):
    if idx == k:
        # 최소 1개에서 최대 p개 사용 조건 충족 여부 + 변경이후 값이 1과 n이내인지 체크 
        if P > p >= 0 and 0 < int(after) <= n:
            cases.append(after)
        return
    for i in range(10):
        diff = bin(display[int(x2digit[idx])] ^ display[i])
        count = sum([1 for d in diff[2:] if d == '1'])
        if count <= p and idx < k:
            dfs(x2digit, idx + 1, p-count, after + str(i))

dfs(x2digit, 0, P, '')
print(len(cases))
# 비트마스킹 활용해서 반전해야 하는 자릿수 수를 획득
# 이후 dfs를 통해 만족하는 결과를 출력하면 됨
# pypy3: 800ms / python3: 1360ms