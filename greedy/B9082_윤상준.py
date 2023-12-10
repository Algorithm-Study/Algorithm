t = int(input())
for _ in range(t):
    n = int(input())
    info = [int(x) for x in list(input())]
    hint = input()
    if n % 3 == 0:
        print(sum([info[x] for x in range(1,n,3)]))
    else:
        print(sum([info[x] for x in range(0,n,3)]))