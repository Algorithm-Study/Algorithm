def solution(n, words):
    # 초기값 설정
    words_book = set()
    key_letter = words[0][0]
    
    for idx, word in enumerate(words):
        # 사용한 단어거나 끝말잇기가 아니라면 탈락 결과 반환
        if word in words_book or key_letter != word[0]:
            return idx%n + 1, idx//n + 1
        # 새로운 단어 추가 및 끝말 저장
        words_book.add(word)
        key_letter = word[-1]
    # 탈락자 없이 끝났다면 탈락자 없음을 반환
    return 0, 0