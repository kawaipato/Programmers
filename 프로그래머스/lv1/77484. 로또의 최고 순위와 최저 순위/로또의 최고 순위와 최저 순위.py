def solution(lottos, win_nums):
    zero = lottos.count(0)
    rule = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    n = 0
    for l in lottos:
        n += win_nums.count(l)
    return (rule[n+zero],rule[n])