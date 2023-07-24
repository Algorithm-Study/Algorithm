n, m = map(int, input().split())

know = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if know.intersection(party):
            know = know.union(party)
            
answer = 0
for party in parties:
    if know.intersection(party):
        continue
    
    answer += 1
    
print(answer)