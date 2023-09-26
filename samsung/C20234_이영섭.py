import heapq
from collections import defaultdict

grader = []
g_num = 0
waiting_queue = []
waiting_queue_dict = defaultdict(int)
dm = defaultdict(int)


def grader_init(n, domain, pid):
    global grader
    grader = [0]*n
    heapq.heappush(waiting_queue, (1, 0, domain, pid))
    waiting_queue_dict[(domain, pid)] = 1


def grading_request(t, p, domain, pid):
    if waiting_queue_dict[(domain, pid)] == 0:
        heapq.heappush(waiting_queue, (p, t, domain, pid))
        waiting_queue_dict[(domain, pid)] = 1


def grading_attempt(st):
    global g_num
    # print("g_num", g_num)
    if len(waiting_queue) == 0:
        return
    p, t, domain, pid = heapq.heappop(waiting_queue)
    if g_num >= len(grader) or dm[domain] > st:
        heapq.heappush(waiting_queue, (p, t, domain, pid))
        return
    waiting_queue_dict[(domain, pid)] = 0
    grader[g_num] = (domain, st)
    while g_num < len(grader) and grader[g_num] != 0:
        g_num += 1


def grading_ends(t, jid):
    global g_num
    if grader[jid] == 0:
        return
    domain, st = grader[jid]
    grader[jid] = 0
    dm[domain] = st + (t - st) * 3
    if jid < g_num:
        g_num = jid


def check_queue():
    return len(waiting_queue)


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