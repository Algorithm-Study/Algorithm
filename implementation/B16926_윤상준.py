N,M,R=map(int,input().split())

field=[list(map(int,input().split()))for _ in range(N)]

for k in range(R):
    s=min(N,M)//2
    for j in range(s):
        x,y=j,j
        pre=field[x][y]
        #좌변
        for i in range(x+1,N-j):

            tmp=field[i][j]
            field[i][j]=pre
            pre=tmp
        #아랫변
        for i in range(y+1,M-j):

            tmp=field[N-1-j][i]
            field[N-1-j][i]=pre
            pre=tmp
        #우측변
        for i in range(N-j-2,j-1,-1):

            tmp=field[i][M-1-j]
            field[i][M-1-j]=pre
            pre=tmp
        #윗변
        for i in range(M-2-j,j-1,-1):

            tmp=field[j][i]
            field[j][i]=pre
            pre=tmp

for i in range(N):
    for j in range(M):
        print(field[i][j],end=' ')
    print()