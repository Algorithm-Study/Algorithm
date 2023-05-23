t = int(input())
def palindrome(word, left, right):
    while left< right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
for _ in range(t):
    word = input()
    left, right = 0, len(word)-1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        elif palindrome(word, left+1, right) or palindrome(word,left,right-1):
            print(1)
            break
        else:
            print(2)
            break
    if left >= right:
        print(0)
