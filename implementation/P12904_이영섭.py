def isPalindrome(x):
    if x==x[::-1]:
        return True
def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]):
                if answer < len(s[i:j]):
                    answer = len(s[i:j])
    return answer