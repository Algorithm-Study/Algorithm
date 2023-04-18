from collections import deque
import sys
input = sys.stdin.readline

#입력
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    #bfs탐색
    visit = [False]*10000
    queue = deque([(A, "")])
    visit[A] = True
    while queue:
        n, x = queue.popleft() #숫자, 연산

        # B와 같다면 BFS탐색 종료
        if n == B:
            print(x)
            break

        #아니라면 DSLR 연산
        #D연산
        num = (n*2) % 10000
        if not visit[num]:
            visit[num] = True #방문
            queue.append((num, x + 'D'))

        #S연산
        num = (n-1) if n != 0 else 9999 #n-1, 단 0이면 9999
        if not visit[num]:
            visit[num] = True #방문
            queue.append((num, x + 'S'))

        #L연산
        num = (n%1000)*10 + n//1000 #천의 자리를 떼서 뒤에 붙임
        if not visit[num]:
            visit[num] = True #방문
            queue.append((num, x + 'L'))

        #R연산
        num = n//10 + (n%10)*1000 #일의 자리를 떼서 앞에 붙임
        if not visit[num]:
            visit[num] = True #방문
            queue.append((num, x + 'R'))

# 처음에 dfs로 시도해서 처음 방향을 완전히 잘못 잡았다
# ref https://star7sss.tistory.com/293?category=913187