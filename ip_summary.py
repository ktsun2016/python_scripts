# comment
def ip_summary(ip1, ip2):
    ip1_bin=['{:08b}'.format(int(i)) for i in ip1.split('.')]
    ip2_bin=['{:08b}'.format(int(i)) for i in ip2.split('.')]
    for i in range(4):
        for j in range(8):
            if ip1_bin[i][j] != ip2_bin[i][j]:
#                 print(i,j,'hit inner break')
                break
        else:
#             print(i,j,'reach here')
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
    return ip_new, prefix_length

ip1='192.168.1.0'
ip2='192.168.2.0'        
result=ip_summary(ip1,ip2)
print('IP1: {}, IP2: {} summarized subnet: {}, prefix: {}'.format(ip1, ip2, result[0], result[1]))

def ip_summary_plus(ip_list):
    if len(ip_list)<2:
        print('ip list is not valid')
    else:
        ip_out=ip_list[0]
        for i in range(len(ip_list)-1):
            ip_out=ip_summary(ip_out, ip_list[i+1])[0]
    return ip_out
ip_list=['192.168.1.0', '192.168.2.0', '192.168.3.0']
#ip_summary_plus(ip_list)
print('IP list {} summarized subnet: {}'.format(ip_list,ip_summary_plus(ip_list)))
