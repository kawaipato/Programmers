import math
def solution(n, k):
    people, ans = [i for i in range(1,n+1)], []
    k -= 1
    for i in range(n,0,-1):
        fact = math.factorial(i-1)
        ans.append(people.pop(k//fact))
        k %= fact
        
    return ans