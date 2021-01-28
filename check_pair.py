def check_pair(s):
    i=0
    if len(s) % 2 !=0:
        return False
    else:
        pass
    s1=list(s)
    
    if "(" in s1 and ")" in s1:
        l1=[i for i,x in enumerate(s1) if x=='(']
        l2=[i for i,x in enumerate(s1) if x==')']
        if len(l1) != len(l2):
            return False
        else:
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return False
                else:
                    pass
    if "[" in s1 and "]" in s1:
        l3=[i for i,x in enumerate(s1) if x=='[']
        l4=[i for i,x in enumerate(s1) if x==']']
        if len(l3) != len(l4):
            return False
        else:
            for i in range(len(l3)):
                if l3[i] > l4[i]:
                    return False
                else:
                    pass
    if "{" in s1 and "}" in s1:
        l5=[i for i,x in enumerate(s1) if x=='{']
        l6=[i for i,x in enumerate(s1) if x=='}']
        if len(l5) != len(l6):
            return False
        else:
            for i in range(len(l5)):
                if l5[i] > l6[i]:
                    return False
                else:
                    pass
    return True

s="([])[]({})"
print(check_pair(s))
