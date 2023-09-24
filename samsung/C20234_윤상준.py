import heapq
import sys
# 최대 도메인 수. 채점기 수, ㅑINF 지정
MAX_DOMAIN = 300
MAX_MARKER = 50000
INF = sys.maxsize
# 도메인 별 레디 큐 생성
waiting_queue = [set() for _ in range(MAX_DOMAIN + 1)]
# 각 채점기들의 채점 중 도메인 저장(0: 채점 안 하는 중)
judging_domain = [0 for _ in range(MAX_MARKER + 1)]
# 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리합니다.
domain_history = [[0,0,0] for _ in range(MAX_DOMAIN + 1)]
# 도메인을 순서대로 저장할 수 있도록 변환 딕셔너리 생성
domain2Idx = {}
cnt = 0
# 대기 큐에 저장된 테스크의 수
ans = 0
# 각 도메인 별 문제ID 저장
domain_queue = [[] for _ in range(MAX_DOMAIN + 1)]
# 명령 실행
q = int(input())
for _ in range(q):
    query = input().split()
    # 채점기 준비
    if int(query[0]) == 100:
        op, n, url = query
        n = int(n)
        marker = [x for x in range(1,n+1)]
        domain, num = url.split('/')
        if domain not in domain2Idx:
            cnt += 1
            domain2Idx[domain] = cnt
        domain_idx = domain2Idx[domain]
        waiting_queue[domain_idx].add(num)
        # 우선순위, 시간, 문제번호
        newUrl = (1, 0, num)
        heapq.heappush(domain_queue[domain_idx],newUrl)
        ans += 1
    # 채점 요청
    if int(query[0]) == 200:
        op, t, p, url = query
        t = int(t)
        p = int(p)
        domain, num = url.split('/')
        # 새로운 도메인인 경우
        if domain not in domain2Idx:
            cnt += 1
            domain2Idx[domain] = cnt
        domain_idx = domain2Idx[domain]
        # 이미 해당 url로 요청이 된 경우 거부
        if num in waiting_queue[domain_idx]:
            continue
        waiting_queue[domain_idx].add(num)
        newUrl = (p, t, num)
        heapq.heappush(domain_queue[domain_idx],newUrl)
        ans += 1
    # 채점 시도
    if int(query[0]) == 300:
        op, t = query
        t = int(t)
        # 채점 가능한 채점기가 없으면 패스
        if not marker:
            continue
        min_domain = 0
        minUrl = (INF, 0, 0)
        for i in range(1,cnt+1):
            # 도메인 작업이 진행되고 있는 경우 패스
            if domain_history[i][2] > t:
                continue
            if domain_queue[i]:
                curUrl = domain_queue[i][0]
                # 튜플 부등식을 활용해 우선 순위 처리
                if minUrl > curUrl:
                    minUrl = curUrl
                    min_domain = i
        # 가능한 것을 선택한 경우
        if min_domain:
            judger_idx = heapq.heappop(marker)
            heapq.heappop(domain_queue[min_domain])
            domain_history[min_domain] = [t,0,INF]
            judging_domain[judger_idx] = min_domain
            waiting_queue[min_domain].remove(minUrl[2])
            ans -= 1
    # 채점 종료
    if int(query[0]) == 400:
        op, t, id = query
        t = int(t)
        id = int(id)
        # 이미 종료 상태인 경우
        if judging_domain[id] == 0:
            continue
        heapq.heappush(marker, id)
        domain_idx = judging_domain[id]
        judging_domain[id] = 0
        domain_history[domain_idx][1] = t - domain_history[domain_idx][0]
        domain_history[domain_idx][2] = domain_history[domain_idx][0] + 3*domain_history[domain_idx][1]
    #채점 대기 큐 조회
    if int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url의 개수를 출력해줍니다.
        op, t= query
        print(ans)
# 걸린시간: 3시간+
# 알게된점
# 튜플 부등식을 통한 우선순위 체크하여 다음에 채점할 문제 선정
# 구현만 할 수 있으면 기존 삼성 유형 대비 쉬움
# 우선순위 큐를 적극적으로 활용 해야 함