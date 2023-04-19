N, M = map(int, input().split())
word_book = {}

for _ in range(N):
    word = input()
    if word in word_book:
        word_book[word] += 1
    else:
        word_book[word] = 1

new_list = sorted(word_book.items(), key= lambda x: [-x[1], -len(x[0]), x[0]])
for nl in new_list:
    if len(nl[0]) >= M:
        print(nl[0])