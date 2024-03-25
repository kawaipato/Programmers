answer = 0
def solution(begin, target, words):
    def dfs(begin, target, words, cnt):
        global answer
        if begin == target:
            answer = cnt
        for idx, word in enumerate(words):
            if sum(a != b for a, b in zip(begin,word)) == 1:
                new_words = words[:idx] + words[idx+1:]
                dfs(word, target, new_words, cnt + 1)
    dfs(begin,target,words,0)            
    return answer