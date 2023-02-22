string = input()
bomb = input()

bomb_last_s = bomb[-1]
stack = []
bomb_length = len(bomb)

for char in string:
    stack.append(char)
    if char == bomb_last_s and ''.join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)