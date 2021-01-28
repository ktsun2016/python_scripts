def check_first(s, c1, c2):
    if c1 in s and c2 in s:
        l1=[i for i,x in enumerate(s) if x==c1]
        l2=[i for i,x in enumerate(s) if x==c2]
        if len(l1) != len(l2):
            return False
        else:
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return False
                else:
                    pass
    return True
def check_pair(s):
    if len(s) % 2 !=0:
        return False
    else:
        pass
    s1=list(s)
    if check_first(s1, '(',')') and check_first(s1, '{','}') and check_first(s1, '[',']'):
        return True
    else:
        return False
    
s="([])[]({}))("
print(check_pair(s))
