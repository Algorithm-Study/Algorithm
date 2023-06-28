N, R, C = map(int, input().split())

def sol(n, r, c, ans):
    d = [[0, 1], [2, 3]]
    ans += (2**(2*n-2))*d[r//2**(n-1)][c//2**(n-1)]
    if n == 1:
        return ans
    else:
        r %= 2**(n-1)
        c %= 2**(n-1)
        n -= 1
        return sol(n, r, c, ans)
    
    
print(sol(N, R, C, 0))
