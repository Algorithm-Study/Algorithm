from sortedcontainers import SortedSet, SortedDict
import heapq
import sys

class Priority_Q:
    def __init__(self) -> None:
        # 생성자로 빈 리스트 생성
        self.items = []
        
    def push(self, item):
        # push 구현
        heapq.heappush(self.items, item)

    def empty(self):
        # is_empty 구현
        return not self.items
    
    def size(self):
        # 큐 데이터 수 반환
        return len(self.items)

    def pop(self):
        # 최솟값 pop 구현
        if self.empty():
            raise Exception("Queue is empty")
        
        return heapq.heappop(self.items)
    
    def top(self):
        # 최솟값 확인
        if self.empty():
            raise Exception("Queue is empty")

        return self.items[0]

MAX_D = 300
MAX_N = 50000
INF = sys.maxsize

# 해당 도메인에서 해당 문제ID가 레디큐에 있는지 관리
is_in_readyq = [SortedSet() for _ in range(MAX_D+1)]

# 현재 쉬고 있는 채점기들을 관리
rest_judger = Priority_Q()

# 각 채점기들이 채점할 때 도메인의 인덱스 저장
judging_domain = [0 for _ in range(MAX_N+1)]

# 각 도메인별 start, gap, end(채점이 가능한 최소 시간)을 관리
s = [0 for _ in range(MAX_D+1)]
g = [0 for _ in range(MAX_D+1)]
e = [0 for _ in range(MAX_D+1)]

# 도메인을 관리하기 위해 cnt 이용
# 도메인 문자열을 int로 변환해주는 map 관리
domainToIdx = SortedDict()
cnt = 0

# 현재 채점 대기 큐에 있는 task의 개수를 관리합니다.
answer = 0

# 각 도메인별 우선 순위 큐를 생성
# 우선 순위가 가장 높은 url을 뽑는다
url_pq = [Priority_Q() for _ in range(MAX_D+1)]

# 채점기 준비
def init(query):
    global n
    empty, n, url = query
    n = int(n)
    
    global cnt

    for i in range(1, n+1):
        rest_judger.push(i)

    # url에서 도메인, 숫자로 분리
    tmp = url.split('/')
    domain, num = tmp[0], int(tmp[1])
    
    # 만약 도메인이 처음 나온 도메인이면 domainToIdx 갱신
    if not domain in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
    domain_idx = domainToIdx[domain]
    
    # 도메인 번호에 맞는 레디큐에 숫자 부분을 넣는다
    is_in_readyq[domain_idx].add(num)
    
    # 새로 들어온 url을 도메인에 맞춰 url.pq에 넣는다
    # id, tme, num
    newUrl = (1, 0, num)
    url_pq[domain_idx].push(newUrl)
    
    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가
    global answer
    answer += 1
    
    
# 새로운 url을 입력받아 레디큐에 추가
def NewUrl(query):
    empty, tme, id, url = query
    tme = int(tme)
    id = int(id)

    global cnt
    
    # url에서 도메인 부분과 숫자 부분을 나눈다        
    tmp = url.split('/')
    domain, num = tmp[0], int(tmp[1])
    
    if domain not in domainToIdx:
        cnt += 1
        domainToIdx[domain] = cnt
        
    domain_idx = domainToIdx[domain]

    # 숫자 부분이 이미 레디큐에 있으면 중복이므로 패스
    if num in is_in_readyq[domain_idx]:
        return
    
    # 도메인 번호에 맞는 레디큐에숫자 부분을 넣는다
    is_in_readyq[domain_idx].add(num)

    # 새로 들어온 url을 도메인에 맞춰 url_pq에 넣는다
    newUrl = id, tme, num
    url_pq[domain_idx].push(newUrl)
    
    # 채점 대기 큐에 값이 추가됐으므로 개수를 1 추가
    global answer
    answer += 1
    
# 다음 도메인을 찾아 assign
def Assign(query):
    empty, tme = query[0], int(query[1])
    
    # 쉬고 있는 채점기가 없으면 넘어감
    if rest_judger.empty():
        return
    
    # 가장우선순위가 높은 url
    min_domain = 0
    minUrl = INF, 0, 0
    
    global cnt
    
    for i in range(1, cnt+1):
        # 만약 현재 채점중이거나, 현재 시간에 이용할 수 없다면 넘어감
        if e[i] > tme:
            continue
        
        # 만약 i번 도메인에 해당하는 url이 존재하면
        # 해당 도메인에서 가장 우선순위가 높은 url을 뽑고 갱신
        if not url_pq[i].empty():
            curUrl = url_pq[i].top()
            
            if minUrl > curUrl:
                minUrl = curUrl
                min_domain = i
                
        
    # 만약 가장 우선순위가 높은 url이 존재하면
    # 해당 도메인과 쉬고 있는 가장 낮은 번호의 채점기 연결
    if min_domain:
        judger_idx = rest_judger.top()
        rest_judger.pop()
        
        # 해당 도메인의 가장 우선순위가 높은 url을 지운다
        url_pq[min_domain].pop()
        
        # 도메인의 start, end를 갱신
        s[min_domain] = tme
        e[min_domain] = INF
        
        # judger_idx번 채점기가 채점하고 있는 도메인 번호를 갱신
        judging_domain[judger_idx] = min_domain
        
        # 레디큐에서 해당 url의 숫자를 지운다
        is_in_readyq[min_domain].remove(minUrl[2])
        
        # 채점 대기 큐에 값이 지워졌으므로 개수 1 감소
        global answer
        answer -= 1
            
# 채점기 마무리        
def Finish(query):
    empty, tme, id = query[0], int(query[1]), int(query[2])

    # 만약 id번 채점기가 채점 중이 아닐 경우 스킵
    if judging_domain[id] == 0:
        return
    
    # id번 채점기를 마무리
    rest_judger.push(id)
    domain_idx = judging_domain[id]
    judging_domain[id] = 0
    
    # 해당 도메인의 gap, end 값을 갱신
    g[domain_idx] = tme - s[domain_idx]
    e[domain_idx] = s[domain_idx] + 3*g[domain_idx]

    
# 현재 채점 대기 큐에 있는 url의 개수 출력
def Check(query):
    empty, tme = query[0], int(query[1])

    global answer
    print(answer)

    
q = int(input())

for _ in range(q):
    query = input().split()

    if int(query[0]) == 100:
        # 채점기 준비
        init(query)
    elif int(query[0]) == 200:
        # 새로운 url 레디큐에 추가
        NewUrl(query)
    elif int(query[0]) == 300:
        # 다음 도메인을 찾아 assign
        Assign(query)
    elif int(query[0]) == 400:
        # 채점 하나 마무리
        Finish(query)
    else: # int(query[0]) == 500:
        # 현재 채점 대기 큐에 있는 url 개수 출력
        Check(query)