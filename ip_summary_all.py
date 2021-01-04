def ip_bin(ip):
    '''
    conver ip1 and ip2 string in decimal into a 4 8-bit list in binary 
    1. split an ip address string by '.' into a list
    2. tun each octet (i) to a 8-bit bianry by bin(int(i)+2560[3:]
    3. exclude the last '.'
    
    '''
    # task 1
    ip=ip.split('.') 
    
    # task 2
    ip_new=''
    for i in ip:
        ip_new=ip_new+bin(int(i)+256)[3:]+'.' 
        
    # task 3
    return ip_new[:-1] # exclude the last '.'

print(ip_bin('192.168.1.0'))
def ip_summary(ip1, ip2):
    '''
    
    1. Data conversion:
        conver ip1 and ip2 string in decimal into a 4 8-bit list in binary 
    2. Data comparison:
        a. compare ip1 with ip2 in binary bit by bit and get the total number of bit in common
        b. identify which octet (i) and which bit in this octet (j)
        c. the construct of for/else/break is used to loop thru the comparison
    3. Rebuid the network address:
        a. the octet of the new network address is the same as the ref network address 
           if the octet is less than target octet (i)
        b. the octet of the new network address will be all 'o' if the octet is larger that the 
           target octet (i)
        c. in case of the octet is the same as the target octet, find the new ocet based on the 
           the value of the bit (j)
           i. if the bit index is less than j, then the bit value is '1'
           ii. if the bit index is larger or equal to j, then the bit value is '0'
    4. the prefix value will be 8*i+j
    
    '''
    # task 1
    ip_ref=ip1.split('.') # use to create the target network address
    ip1_bin=ip_bin(ip1).split('.')
    ip2_bin=ip_bin(ip2).split('.')
    
    # task 2
    for i in range(4):
        for j in range(8):
            if ip1_bin[i][j] != ip2_bin[i][j]:
                break
        else:
            continue # continue if inner loop does not break
        break  # break if inner loop does break
    # task 3
    new_ip=[]
    for k in range(4):
        if k < i:
            new_ip.insert(k, ip_ref[k])
        if k > i:
            new_ip.insert(k, '0')
        if k==i:
            bin1=''
            for l in range(8):
                if l < j:
                    bin1=bin1+ip1_bin[k][l]
                else:
                    bin1=bin1+'0'
            new_ip.insert(k, str(int(bin1, 2)))
    new_ip='.'.join(new_ip)
    # task 4
    prefix=8*i+j
    
    return new_ip, prefix

ip1= '192.168.1.0'
ip2= '192.168.2.0'

print('ip1 {} and ip2 {} summaried is'.format(ip1,ip2),ip_summary(ip1, ip2))
def ip_summary_plus(ip):
    while len(ip)>1:
        final_ip=ip[0]
        for i in range(len(ip)):
            final_ip=ip_summary(final_ip, ip[i])[0]
        return final_ip
ip=['192.168.1.0', '192.168.2.0', '192.169.0.0', '192.167.0.0']
print('ip list {} summaried as'.format(ip),ip_summary_plus(ip))
