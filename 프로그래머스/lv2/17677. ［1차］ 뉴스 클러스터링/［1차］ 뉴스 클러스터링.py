def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if str1 > str2:
        str1, str2 = str2, str1
    str2_copy = str2.copy()
    it = []
    for s in str1:
        if s in str2_copy:
            it.append(s)
            str2_copy.remove(s)
    if len(str1 + str2) == 0:
        return 65536
    else:
        return int(65536 * (len(it)/(len(str1) + len(str2) - len(it))))