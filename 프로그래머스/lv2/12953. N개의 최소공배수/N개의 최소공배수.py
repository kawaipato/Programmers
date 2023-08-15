from math import gcd
def solution(arr):
    def lcm(a,b):
        return (a*b) // gcd(a,b)
    
    while True:
        arr.append(lcm(arr.pop(),arr.pop()))
        print(arr)
        if len(arr) == 1:
            return arr[0]