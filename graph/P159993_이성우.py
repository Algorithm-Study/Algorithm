from collections import deque

def get_cnt(maps,start,end):
    """ 입력받은 시작점부터 문자까지의 최소거리와 문자위치 계산 함수 """
    r,c = start # 시작위치
    N,M = len(maps),len(maps[0]) # 맵크기

    # BFS
    visited = set()
    # cnt를 따로 추가하여 map을 변경하지 않고도 해결했음
    q = deque([(r,c,0)])
    directions = ((1,0),(0,1),(-1,0),(0,-1))

    while q:
        now_r,now_c,cnt = q.popleft()
        if (now_r,now_c) in visited: # 방문했다면 패스
            continue
        else: # 그렇지 않다면 추가
            # visited map을 만들지 않고 지나간 좌표를 체크해두는 것으로 해결함
            visited.add((now_r,now_c))
            if maps[now_r][now_c] == "X": # 현 문자가 X면 패스
                continue
            elif (now_r,now_c) == end: # 도착점이면 현위치,거리 리턴
                return cnt
            else: # 아니라면 네 방향중 맵 크기 안쪽 위치를 deque에 추가
                for dr,dc in directions:
                    next_r,next_c = now_r+dr,now_c+dc
                    if 0<=next_r<N and 0<=next_c<M:
                        q.append((next_r,next_c,cnt+1))
                        
    # 다 돌면 도착 지점에 접근을 못한 것이므로 -1 반환
    return -1 # 문자에 접근 불가능한 경우


def solution(maps):
    S_pos,L_pos,E_pos = None,None,None
    # S,L,E의 위치 찾기
    for i,row in enumerate(maps):
        if "S" in row:
            # find 함수로 좌표값 쉽게 반환
            S_pos = (i,row.find("S"))
        if "L" in row:
            L_pos = (i,row.find("L"))
        if "E" in row:
            E_pos = (i,row.find("E"))

    # 시작점~레버의 거리 계산
    lever_cnt = get_cnt(maps,start=S_pos,end=L_pos)
    if lever_cnt == -1:
        return -1

    # 레버위치~출구 거리 계산
    exit_cnt = get_cnt(maps,start=L_pos,end=E_pos)
    return exit_cnt+lever_cnt if exit_cnt != -1 else -1