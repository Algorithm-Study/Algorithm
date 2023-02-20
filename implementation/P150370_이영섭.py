dict = {}

def date_to_int(date):
    new_date = date.split(".")
    int_date = int(new_date[0])*12*28 + int(new_date[1])*28 + int(new_date[2])
    return int_date

def terms_to_dict(terms):
    for term in terms:
        temp = term.split()
        dict[temp[0]] = temp[1]

def solution(today, terms, privacies):
    answer = []
    today_date = date_to_int(today)
    print(f"today: {today_date}")
    terms_to_dict(terms)
    for idx, pri in enumerate(privacies):
        text = pri.split()
        month = dict[text[1]]
        pri_date = date_to_int(text[0])
        yuhyo = pri_date + int(month)*28 - 1
        print(f"yuhyo: {yuhyo}")
        if(yuhyo < today_date):
            answer.append(idx+1)
    return answer