from collections import Counter
def solution(keymap, targets):
    ans = []
    for target in targets:
        counter = Counter(target)
        cnt, error = 0, 0
        for tar in counter:
            try : 
                cnt += min([key.find(tar) + 1 for key in keymap if key.find(tar) + 1 != 0]) * counter[tar]
            except:
                error += 1
        ans.append(cnt) if error == 0 else ans.append(-1)
    return ans