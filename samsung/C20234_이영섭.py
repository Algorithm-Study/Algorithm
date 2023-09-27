import heapq
from collections import defaultdict

grader = []
grader_dict = defaultdict(int)
g_num = 0
waiting_queue = defaultdict(list)
waiting_queue_dict = defaultdict(int)
dm = defaultdict(int)


def grader_init(n, domain, pid):
    global grader
    grader = [0]*n
    heapq.heappush(waiting_queue[domain], (1, 0, pid))
    waiting_queue_dict[(domain, pid)] = 1


def grading_request(t, p, domain, pid):
    if waiting_queue_dict[(domain, pid)] == 0:
        heapq.heappush(waiting_queue[domain], (p, t, pid))
        waiting_queue_dict[(domain, pid)] = 1


def grading_attempt(st):
    global g_num
    if g_num >= len(grader):
        return
    min_url = (float('inf'), float('inf'))
    min_domain = ''

    for key in waiting_queue.keys():
        if len(waiting_queue[key]) == 0 or grader_dict[key] == 1 or dm[key] > st:
            continue
        item = min(waiting_queue[key])
        if item[:2] < min_url:
            min_url = item[:2]
            min_domain = key

    if min_url != (float('inf'), float('inf')):
        p, t, pid = heapq.heappop(waiting_queue[min_domain])
        waiting_queue_dict[(min_domain, pid)] = 0
        grader[g_num] = (min_domain, st)
        grader_dict[min_domain] = 1
        while g_num < len(grader) and grader[g_num] != 0:
            g_num += 1


def grading_ends(t, jid):
    global g_num
    if grader[jid] == 0:
        return
    domain, st = grader[jid]
    grader[jid] = 0
    grader_dict[domain] = 0
    dm[domain] = st + (t - st) * 3
    if jid < g_num:
        g_num = jid
    # print("g_num", g_num)


def check_queue():
    cnt = 0
    for key in waiting_queue.keys():
        cnt += len(waiting_queue[key])
    return cnt


q = int(input())
for _ in range(q):
    code = input().split()
    if int(code[0]) == 100:
        domain, pid = code[2].split('/')
        grader_init(int(code[1]), domain, pid)

    elif int(code[0]) == 200:
        domain, pid = code[3].split('/')
        grading_request(int(code[1]), int(code[2]), domain, pid)

    elif int(code[0]) == 300:
        grading_attempt(int(code[1]))

    elif int(code[0]) == 400:
        grading_ends(int(code[1]), int(code[2]) - 1)

    elif int(code[0]) == 500:
        print(check_queue())
    # print(waiting_queue)
    # print(grader)
    # print(dm)