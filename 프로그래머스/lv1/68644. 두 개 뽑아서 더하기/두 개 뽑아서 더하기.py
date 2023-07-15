def solution(numbers):
    a=[]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            a.append(numbers[i] + numbers[j])
    return sorted(list(set(a)))