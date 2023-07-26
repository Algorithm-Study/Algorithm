from collections import deque

n = int(input())
word = input()
words = [word]
tmp = word

while True:
    stack = []
    dq = deque()
    for idx, letter in enumerate(tmp):
        if idx%2 == 0:
            stack.append(letter)
        else:
            dq.appendleft(letter)
    stack.extend(dq)
    tmp = ''.join(stack)
    words.append(tmp)
    
    if words[-1] == word:
        break
    
print(words[n % (len(words)-1)])