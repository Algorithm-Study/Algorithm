n, k = map(int, input().split())
word = list(input())
stack = [word[0]]
for w in word[1:]:
    while int(stack[-1]) < int(w) and k != 0:
        stack.pop()
        k -= 1
        if not stack:
            break
    stack.append(w)
while k != 0:
    stack.pop()
    k -= 1
print(''.join(stack))

# 첫 for 문 과정에서 K가 다 소진되지 않는 경우가 존재
# for 문 이후 k가 다 소진될 수 있도록 문제 설정해야 함