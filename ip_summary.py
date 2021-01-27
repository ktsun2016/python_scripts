def ip_summary(ip1, ip2):
    ip1_bin=['{:08b}'.format(int(i)) for i in ip1.split('.')]
    ip2_bin=['{:08b}'.format(int(i)) for i in ip2.split('.')]
    for i in range(4):
        for j in range(8):
            if ip1_bin[i][j] != ip2_bin[i][j]:
                print(i,j,'hit inner break')
                break
        else:
            print(i,j,'reach here')
            continue
        break
    prefix_length=8*i+j
    ip_new=[]
    for k in range(4):
        if k<i:
            ip_new.insert(k, ip1.split('.')[k])
        if k>i:
            ip_new.insert(k, '0')
        if k==i:
            bin1=''
            for l in range(8):
                if l < j:
                    bin1=bin1+ip1_bin[k][l]
                else:
                    bin1=bin1+'0'
            ip_new.insert(k, str(int(bin1,2)))
    ip_new='.'.join(ip_new)
    return prefix_length, ip_new

ip1='192.168.1.0'
ip2='192.168.2.0'        
result=ip_summary(ip1,ip2)
print('summarized subnet: {}, prefix: {}'.format(result[1], result[0]))
