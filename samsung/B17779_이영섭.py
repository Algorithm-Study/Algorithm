import sys
input = sys.stdin.readline
N = int(input())
m = [[0] * (N + 2) for _ in range(N + 2)]
tmp = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        m[i + 1][j + 1] = tmp[i][j]


def get_people(i, j, d1, d2):
    for t in range(1, N + 1):
        if t < i:
            people[1] += sum(m[t][:j + 1])
            people[2] += sum(m[t][j + 1:])
        if i <= t < i + d1:
            people[1] += sum(m[t][:j - (t - i)])
        if i + d1 <= t <= i + d1 + d2:
            people[3] += sum(m[t][:j - d1 + d2 - (i + d1 + d2 - t)])
        if i <= t <= i + d2:
            people[2] += sum(m[t][j + (t - i) + 1:])
        if i + d2 < t <= i + d1 + d2:
            people[4] += sum(m[t][j - d1 + d2 + (i + d1 + d2 - t) + 1:])
        if i + d1 + d2 < t:
            people[3] += sum(m[t][:j - d1 + d2])
            people[4] += sum(m[t][j - d1 + d2:])
        if d1 >= d2:
            if i <= t < i + d1:
                people[5] += sum(m[t][j - (t - i): j + (t - i) + 1])
            if i + d1 <= t <= i + d1 + d2:
                people[5] += sum(m[t][j - d1 + d2 - (i + d1 + d2 - t): j - d1 + d2 + (i + d1 + d2 - t) + 1])
        else:
            if i <= t <= i + d1:
                people[5] += sum(m[t][j - (t - i): j + (t - i) + 1])
            if i + d1 < t <= i + d1 + d2:
                people[5] += sum(m[t][j - d1 + d2 - (i + d1 + d2 - t): j - d1 + d2 + (i + d1 + d2 - t) + 1])


ans = float('inf')
for i in range(1, N - 1):
    for j in range(1, N - 1):
        for d1 in range(1, N - 1):
            if i + d1 > N - 1 or j - d1 < 0:
                break
            for d2 in range(1, N - 1):
                people = [0, 0, 0, 0, 0, 0]
                if i + d2 > N or j + d2 > N:
                    break
                get_people(i, j, d1, d2)
                diff = max(people[1:]) - min(people[1:])
                if ans > diff:
                    ans = diff
print(ans)
