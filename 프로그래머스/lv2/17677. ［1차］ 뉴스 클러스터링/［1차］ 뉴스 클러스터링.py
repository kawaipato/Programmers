def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    intersection = set(str1) & set(str2)
    union = set(str1) | set(str2)
    if len(union) == 0:
        return 65536
    inte_sum = sum([min(str1.count(i), str2.count(i)) for i in intersection])
    uni_sum = sum([max(str1.count(u), str2.count(u)) for u in union])
    
    return int(inte_sum/uni_sum * 65536)