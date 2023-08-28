n,m,k=map(int,input().split())
pmap=[[[] for _ in range(n)] for _ in range(n)] # 플레이어들의 맵
gmap=[[[] for _ in range(n)] for _ in range(n)] # 총들의 맵
pos=[] # 플레이어들의 위치 배열
points=[] # 플레이어들의 포인트 배열

class Player: # 플레이어 클래스
    def __init__(self,no,x,y,d,s,g=0):
        self.no=no
        self.x=x
        self.y=y
        self.d=d
        self.s=s
        self.g=g

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        gmap[i][j].append(row[j])

for no in range(m):
    x,y,d,s=map(int,input().split())
    x,y=x-1,y-1
    pos.append([x,y])
    pmap[x][y].append(Player(no,x,y,d,s))
    points.append(0)

def move(nx,ny,player):
    global pmap,pos
    # 플레이어의 위치를 업데이트한다.
    pmap[nx][ny].append(player)
    pmap[player.x][player.y].remove(player)
    player.x,player.y=nx,ny
    pos[player.no]=[player.x,player.y]
    return player
# 총을 잃는다.
def lose(x,y,player):
    global gmap
    if player.g!=0:
        gmap[x][y].append(player.g)
    player.g=0
    return player
# 총을 줍는다.
def get(x,y,player):
    global gmap
    # 총을 잃은 플레이어가
    lost_player=lose(x,y,player)
    # 가장 공격력이 높은 총을
    tg=max(gmap[x][y])
    # 장착한다.
    lost_player.g=tg
    # 해당 총은 총 맵에서 없앤다.
    gmap[x][y].remove(tg)
    return lost_player

for _ in range(k):
    # 각 플레이어들이 각자의 위치에서 순서대로
    for ax,ay in pos:
        # 이번 플레이어
        me=pmap[ax][ay][0]
        # 정면의 칸으로
        me_nx=ax+dx[me.d]
        me_ny=ay+dy[me.d]
        # 만약 정면의 칸이 범위 밖이면, 정반대 방향의 칸으로
        if not (0<=me_nx<n and 0<=me_ny<n):
            me.d=(me.d+2)%4
            me_nx=ax+dx[me.d]
            me_ny=ay+dy[me.d]
        # 이동
        me = move(me_nx, me_ny, me)
        # 만약 이동한 칸에 이번 플레이어만 있다면
        if pmap[me_nx][me_ny][0]==me:
            # 해당 칸에 총이 있다면
            if len(gmap[me.x][me.y])>=1:
                # 총을 줍는다.
                me=get(me.x,me.y,me)
        # 다른 플레이어가 있다면
        else:
            bx,by=me.x,me.y
            # 상대 플레이어
            other=pmap[bx][by][0]
            # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교
            me_sum=me.s+me.g
            other_sum=other.s+other.g
            if me_sum>other_sum:
                winner=me
                loser=other
            elif me_sum<other_sum:
                winner=other
                loser=me
            else:
                if me.s>other.s:
                    winner=me
                    loser=other
                else:
                    winner=other
                    loser=me
            # 이기면 포인트를 얻게 됩니다.
            points[winner.no]+=abs(me_sum-other_sum)
            # 패자는 총을 잃고
            loser=lose(loser.x,loser.y,loser)
            # 다음으로 갈 칸을 선택하는데
            loser_nx,loser_ny=loser.x+dx[loser.d],loser.y+dy[loser.d]
            # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여 빈 칸이 보이면
            if not (0<=loser_nx<n and 0<=loser_ny<n) or len(pmap[loser_nx][loser_ny])!=0:
                while True:
                    loser.d=(loser.d+1)%4
                    loser_nx,loser_ny=loser.x+dx[loser.d],loser.y+dy[loser.d]
                    if (0<=loser_nx<n and 0<=loser_ny<n) and len(pmap[loser_nx][loser_ny])==0:
                        break
            # 이동합니다
            loser=move(loser_nx,loser_ny,loser)
            # 패자가 이동한 칸에 총이 있다면 주움
            if len(gmap[loser.x][loser.y])>=1:
                loser=get(loser.x,loser.y,loser)
            # 승자의 칸에 총이 있다면 주음
            if len(gmap[winner.x][winner.y]) >= 1:
                winner=get(bx,by,winner)
print(*points)