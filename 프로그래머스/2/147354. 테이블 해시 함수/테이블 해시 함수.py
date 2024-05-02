def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end + 1):
        s = 0
        for d in data[i-1]:
            s += d % i
        if answer == 0:
            answer += s
        else:
            answer = answer ^ s
    return answer