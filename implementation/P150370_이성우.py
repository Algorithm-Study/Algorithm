import datetime

def solution(today, terms, privacies):
    answer = []
    today = list(map(int, today.split('.')))
    terms_dict = {}
    for i in terms:
        letter = i.split()[0]
        month = int(i.split()[1])
        terms_dict[letter] = month
        
    for n, privacy in enumerate(privacies):
        privacy_list = list(map(int, privacy.split()[0].split('.')))
        term = privacy.split()[1]
        term = [terms_dict[term]//12, terms_dict[term]%12]
        if privacy_list[2] == 1:
            privacy_list[2] = 28
            privacy_list[1] -= 1
        else:
            privacy_list[2] -= 1
            
        if privacy_list[1] == 0:
            privacy_list[1] = 12
            privacy_list[0] -= 1
            
        if privacy_list[1] + term[1] > 12:
            privacy_list[1] = privacy_list[1] + term[1] - 12
            privacy_list[0] = privacy_list[0] + 1
        else:
            privacy_list[1] += term[1]

        if privacy_list[1] == 0:
            privacy_list[0] -= 1
            privacy_list[1] = 12
        
        privacy_list[0] += term[0]

        if datetime.date(*today) > datetime.date(*privacy_list):
            answer.append(n+1)

    return answer