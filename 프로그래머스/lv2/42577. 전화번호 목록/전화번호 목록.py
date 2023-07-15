from collections import Counter
def solution(phone_book):
    # n = len(min(phone_book))
    # if Counter([p[:n] for p in phone_book]).most_common(1)[0][1]>=2:
    #     return False
    # else:
    #     return True
    p = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if p[i] == p[i+1][:len(p[i])]:
            return False
    return True