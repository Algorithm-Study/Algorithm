from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    result = [10000,0]
    line = input()
    k = int(input())
    infos = defaultdict(list)
    counter = Counter(line)
    for idx,l in enumerate(line):
        if counter[l] >= k:
            infos[l].append(idx)
    if not infos:
        print(-1)
        continue
    for choices in infos.values():
        for i in range(len(choices)- k + 1):
            length = choices[i+k-1] - choices[i] + 1
            result = [min(result[0], length), max(result[1], length)]
    print(*result)
# k개 이상인 애들로 최소, 최대 길이 구하면 되는 문제