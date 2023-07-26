n = int(input())
word = input()
periods = [word]
length = len(word)
count = 0
while True:
    count += 1
    temp = ''
    slice = length//2
    # 섞이는 과정 진행
    for i in range(slice):
        temp += word[i] + word[length-1-i]
    if length % 2 == 1:
        temp += word[slice]
    word = temp
    if periods[0] == word:
        break
    periods.append(word)
print(periods[-n%len(periods)])

# 입력이 십억이므로 시간복잡도에 유의해야 함
# 주기성을 구해서 답을 구해야 함