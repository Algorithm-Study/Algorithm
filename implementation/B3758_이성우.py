import sys
input = sys.stdin.readline

# 총 테스트 케이스 변수 설정
test_case = int(input().rstrip())

for _ in range(test_case):

    # 변수 초기값 설정
    total_team, total_prob, my_team, log = map(int, input().split())
    team_log = [0]*(total_team+1)
    team_submit = [0]*(total_team+1)
    team_score = {}
    for i in range(total_team):
        team_score[i+1] = [0]*(total_prob+1)

    # 주어진 데이터 저장
    for log_idx in range(log):
        team_num, prob_num, score = map(int, input().split())
        team_score[team_num][prob_num] = max(score, team_score[team_num][prob_num])
        team_log[team_num] = log_idx
        team_submit[team_num] += 1
    
    # 조건에 맞게 정렬 후 출력
    rank = list(range(1,total_team+1))
    rank.sort(key = lambda x : [-sum(team_score[x]), team_submit[x], team_log[x]])
    print(rank.index(my_team)+1)