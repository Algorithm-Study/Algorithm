N = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))
men.sort()
women.sort()
st, ed = 0, N-1
ans = 0
while st < N and 0 <= ed:
    if men[st] < 0:
        if women[ed] > 0:
            if abs(men[st]) > abs(women[ed]):
                ans += 1
                st += 1
                ed -= 1
            else:
                ed -= 1
        else:
            st += 1
    else:
        if women[ed] < 0:
            if abs(men[st]) < abs(women[ed]):
                ans += 1
                st += 1
                ed -= 1
            else:
                ed -= 1
        else:
            ed -= 1
print(ans)
# 키가 양수 - 자신보다 키가 큰 사람과 추기를 원함
# 키가 음수 - 자신보다 키가 작은 사람과 추기를 원함
# 양수 < 음수