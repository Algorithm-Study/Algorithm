while True:
    try:
        target = int(input())
        
        n = int(input())
        legos = [int(input()) for _ in range(n)]

        target = target*10000000

        legos.sort()
        left = 0
        right = n-1

        while left < right:
            if legos[left] + legos[right] == target:
                print(f'yes {legos[left]} {legos[right]}')
                break
            elif legos[left] + legos[right] > target:
                right -= 1
            else:
                left += 1
        else:
            print('danger')
    except:
        break