from collections import defaultdict

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        length = defaultdict(int)
        data = []

        for _ in range(n):
            ip = int(input())
            length[ip] += 1
            data.append(ip)
        data.sort()

        for i in data:
            if length[x - i]:
                if i == x - i:
                    if length[i] < 2:
                        continue
                print('yes', min(i, x-i), max(i, x-i))
                break
        else:
            print('danger')
    except:
        break