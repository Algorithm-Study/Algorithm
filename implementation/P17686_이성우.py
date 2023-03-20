import re

def solution(file_names):
    # \D 숫자가 아닌 문자 한 개
    # \d 숫자 한개
    # . 모든 문자
    # + 1개 이상의 패턴
    # * 0개 이상의 패턴
    re_filter = re.compile(r'(\D+)(\d+)(.*)')
    re_files = []
    for file_name in file_names:
        re_files.extend(re_filter.findall(file_name))
    re_files.sort(key=lambda x: (x[0].lower(), int(x[1])))

    answer = [''.join(i) for i in re_files]
    return answer