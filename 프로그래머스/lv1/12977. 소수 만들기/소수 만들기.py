import math
from itertools import combinations
def primenumber(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(nums):
    a, answer =[], 0
    a = combinations(nums,3)
    for i in a:
        if primenumber(sum(i)) == True:
            answer+=1
    return answer