import sys
input = sys.stdin.readline

def is_palindrome(words: str) -> int:
    left = 0
    right = len(words) - 1
    while left < right:
        if words[left] == words[right]:
            left += 1
            right -= 1
        else:
            if left < right - 1:
                temp = words[:right] + words[right + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left + 1 < right:
                temp = words[:left] + words[left + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    else:
        return 0

for _ in range(int(input().rstrip())):
    print(is_palindrome(input().rstrip()))