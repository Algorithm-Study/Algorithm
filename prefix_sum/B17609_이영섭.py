T = int(input())
for _ in range(T):
    n = input()
    left, right = 0, len(n) - 1
    while left < right:
        if n[left] == n[right]:
            left += 1
            right -= 1
        else:
            if left <= right - 1:
                temp = n[:right] + n[right+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            if left + 1 <= right:
                temp = n[:left] + n[left+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            print(2)
            break
    else:
        print(0)

