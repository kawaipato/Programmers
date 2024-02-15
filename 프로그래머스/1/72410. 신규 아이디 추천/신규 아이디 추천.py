import re
def solution(new_id):
    s1 = new_id.lower()
    s2 = re.sub('[^\da-z-_.]','',s1)
    s3 = re.sub('\.+','.',s2)
    s4 = re.sub('^[.]|$[.]','',s3)
    s4 = 'a' if not s4 else s4[:15]
    s4 = s4[:-1] if s4[-1] == '.' else s4
    s4 = s4 if len(s4) > 2 else s4 + ''.join([s4[-1] for i in range(3-len(s4))])
    return s4
    