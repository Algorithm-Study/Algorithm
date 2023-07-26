X = int(input())
word = list(input())
w_len = len(word)
pattern = [word[:]]

while True:
    front = word[:w_len//2+1]
    back = word[w_len//2+1:]
    word = []
    for _ in range(len(back)):
        word.append(front.pop(0))
        word.append(back.pop())
    word += front
    if word == pattern[0]:
        break
    pattern.append(word[:])

pattern = [pattern[0]] + pattern[1:][::-1]
print("".join(pattern[X % len(pattern)]))