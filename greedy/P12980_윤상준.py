#이코테 그리디 챕터의 1이 될때가지와 매우 유사함 p.99
## 효율성 테스트 4, 9 에서 실패 -> 다시 해보니 됨;;
def solution(n):
    ans = 0
    while n > 1: #조건문으로 인해 실패 != 으로 바꾸면 성공
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1

    return ans + 1

## 새로운 접근방식
def solution(n):
    ans = 0
    while True:
        goal = (n //2)*2
        ans += (n-goal)
        n = goal
        if n < 2:
            break
        n //= 2
    return ans + n