def check_pair(s):
    '''
    task1: check the total number of element in this string is
           even, otherwise it should fail.
    '''
    if len(s)%2 !=0:
        return False
    else:
        pass
    
    '''
    task2: locate the index of the two symbols of each pair and check
           1. same occurance
           2. the index of leading symbol is less than its pair symbol
    '''
    
    s1=list(s)
    # task 2.1 for "(" and ")"
    if "(" in s1 and ")" in s1:
        l1=[i for i, x in enumerate(s1) if x == "("]
        l2=[i for i, x in enumerate(s1) if x == ")"]
        if len(l1)!=len(l2):
            return False
        else:
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return False
                else:
                    pass
                
    # task 2.1 for "[" and "]"
    if "[" in s1 and "]" in s1:
        l3=[i for i, x in enumerate(s1) if x == "["]
        l4=[i for i, x in enumerate(s1) if x == "]"]
        if len(l3)!=len(l4):
            return False
        else:
            for i in range(len(l3)):
                if l3[i] > l4[i]:
                    return False
                else:
                    pass
    
    # task 2.1 for "{" and "}"
    if "{" in s1 and "}" in s1:
        l5=[i for i, x in enumerate(s1) if x == "{"]
        l6=[i for i, x in enumerate(s1) if x == "}"]
        if len(l5)!=len(l6):
            return False
        else:
            for i in range(len(l5)):
                if l5[i] > l6[i]:
                    return False
                else:
                    pass
    return True

s='{}()[]'
print(check_pair(s))
