word = input()
stack = []

for w in word:
    stack.append(w)
    if stack[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            stack.pop()

if stack == ['P']:
    print('PPAP')
else:
    print('NP')