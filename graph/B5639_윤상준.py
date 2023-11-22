import sys
sys.setrecursionlimit(10**6)
data = []
while True:
    try:
        data.append(int(input()))
    except:
        break
def p2p(data):
    if not data:
        return
    left, right = data[1:], []
    for i in range(1,len(data)):
        if data[i] > data[0]:
            left, right = data[1:i], data[i:]
            break
    p2p(left)
    p2p(right)
    print(data[0])
p2p(data)