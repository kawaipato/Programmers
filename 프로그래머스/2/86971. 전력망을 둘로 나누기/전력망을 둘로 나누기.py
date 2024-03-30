import copy
def solution(n, wires):
    answer, dic = n, {}
    for w in wires:
        if w[0] in dic:
            dic[w[0]].append(w[1])
        else:
            dic[w[0]] = [w[1]]
        if w[1] in dic:
            dic[w[1]].append(w[0])
        else:
            dic[w[1]] = [w[0]]
    def dfs(i,m):
        result = 1
        for mm in m[i]:
            m[mm].remove(i)
            result += dfs(mm,m)
        return result
    for i in range(1,n+1):
        for nn in dic[i]:
            new_dic = copy.deepcopy(dic)
            new_dic[i].remove(nn)
            new_dic[nn].remove(i)
            answer = min(answer, abs(dfs(i,new_dic) - dfs(nn,new_dic)))           
    return answer