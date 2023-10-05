n, m = map(int, input().split())
locations = list(map(int, input().split()))
negatives = []
positives = []
for l in locations:
    if l < 0:
        negatives.append(l)
    else:
        positives.append(l)
negatives.sort()
positives.sort(reverse = True)
distances= []
for i in range(0, len(negatives),m):
    distances.append(abs(min(negatives[i: i+m])))

for i in range(0, len(positives),m):
    
    distances.append(max(positives[i: i+m])) 
distances.sort()
print(sum(distances[:-1])*2 + distances[-1])