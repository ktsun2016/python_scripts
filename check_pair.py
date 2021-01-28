def check_pair(s):
    
    s1=list(s)
    check=['(',')', '[',']', '{','}']
    check_list=[['(',')'], ['[',']'], ['{','}']]
    for i in range(len(s1)):
        if s1[i] in check:
            pass
        else:
            return False
#     return all(element==s1 for element in check)
    for i in range(len(check_list)):
        if bool(check_list[i][0] in s1) ^ bool(check_list[i][1] in s1):
            return False
        else:
            pass
        if check_list[i][0] in s1 and check_list[i][1] in s1:
            l1=[j for j, x in enumerate(s1) if x==check_list[i][0]]
            l2=[j for j, x in enumerate(s1) if x==check_list[i][1]]
            if len(l1) != len(l2):
                return False
            else:
                for i in range(len(l1)):
                    if l1[i]>l2[i]:
                        return False
                    else:
                        pass
        
    return True
s='{}()[]00'
print(check_pair(s))
