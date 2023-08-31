from collections import Counter
from functools import reduce
def solution(clothes):
    return reduce(lambda x,y:x*y,[x+1 for x in Counter([cloth[1] for cloth in clothes]).values()],1)-1