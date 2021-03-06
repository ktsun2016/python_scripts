import paramiko
import time
import re
import pdb
import sys
#pdb.set_trace()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC

def start_connect(ip, username, password):
        # Create instance of SSHClient object
    remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

    # initiate SSH connection
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print "Interactive SSH session established"

    return remote_conn

def disable_paging(remote_conn):
    '''Disable paging on a Cisco router'''

    remote_conn.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output = remote_conn.recv(1000)

    return output

def send_traffic(remote_conn, fw_net, fw_ip, gw_ip):
    remote_conn.send("route add -net %s gw %s\n" % (fw_net, gw_ip))
    remote_conn.send("route -n\n")
    remote_conn.send("scapy\n")
    remote_conn.send("pingr=IP(dst=\"%s\")/ICMP()\n" % fw_ip)
    remote_conn.send("resp_ping=srloop(pingr,count=5)\n")
    remote_conn.send("resp_ping\n")
    # Wait for the command to complete
    time.sleep(10)
    output = remote_conn.recv(5000)
    remote_conn.send("exit()\n")
    return output


def send_traffic1(remote_conn, fw_net, fw_ip, gw_ip):
    remote_conn.send("route add -net %s gw %s\n" % (fw_net, gw_ip))
    remote_conn.send("route -n\n")
    remote_conn.send("/tmp/traffic1.sh \n")   
    # remote_conn.send("scapy\n")
    # remote_conn.send("pingr=IP(dst=\"%s\")/ICMP()\n" % fw_ip)
    # remote_conn.send("resp_ping=srloop(pingr,count=5)\n")
    # remote_conn.send("resp_ping\n")
    # Wait for the command to complete
    time.sleep(10)
    output = remote_conn.recv(5000)
    remote_conn.send("exit()\n")
    return output

if __name__ == '__main__':


    # VARIABLES THAT NEED CHANGED
    # ip = '172.31.128.90'
    # username = 'root'
    # password = 'embrane'

    # # Create instance of SSHClient object
    # remote_conn_pre = paramiko.SSHClient()

    # # Automatically add untrusted hosts (make sure okay for security policy in your environment)
    # remote_conn_pre.set_missing_host_key_policy(
    #      paramiko.AutoAddPolicy())

    # # initiate SSH connection
    # remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
    # print "SSH connection established to %s" % ip

    # # Use invoke_shell to establish an 'interactive session'
    # remote_conn = remote_conn_pre.invoke_shell()
    # print "Interactive SSH session established"

    # # Strip the initial router prompt
    # output = remote_conn.recv(1000)

    # # See what we have
    # print output
    #start_connect(ip, username, password)


    # Now let's try to send the router a command
    #remote_conn.send("\n")
    #remote_conn.send("show ip int brief\n")
    # fw_net = '172.19.1.0/24'
    # fw_ip='172.19.1.253'
    # gw_ip='6.2.0.1'
    lista = ['172.31.128.90', '172.31.128.90', '172.31.128.91', '172.31.128.91', '172.31.128.92']
    listb = ['root', 'root', 'root', 'root', 'root']
    listc = ['embrane', 'embrane', 'embrane', 'embrane', 'embrane']
    list1 = ['172.19.1.0/24', '192.170.1.0/24', '192.7.1.0/24', '192.5.1.0/24', '192.6.1.0/24']
    list2 = ['172.19.1.253', '192.170.1.253', '192.7.1.252', '192.5.1.252', '192.6.1.252']
    list3 = ['6.2.0.1', '6.2.0.1', '12.1.0.1', '12.1.0.1', '8.1.0.1']

    # lista = ['172.31.128.90']
    # listb = ['root']
    # listc = ['embrane']
    # list1 = ['172.19.1.0/24']
    # list2 = ['172.19.1.253']
    # list3 = ['6.2.0.1']
    for ip, username, password, fw_net, fw_ip, gw_ip in zip(lista, listb, listc, list1, list2, list3):
        rc = start_connect(ip, username, password)
        output = send_traffic(rc, fw_net, fw_ip, gw_ip)
        # print output
        # traffic_pattern=re.compile(r'([ICMP:]\d)')
        # matches = traffic_pattern.finditer(output)
        # for match in matches:
        #     print(match.group(0))
        #output = str(output)
        #print output
        pattern1 = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        output = pattern1.sub('', output)
        traffic_pattern=re.compile(r'Results: TCP:0 UDP:0 ICMP:([1-9])')
        matches = traffic_pattern.finditer(output)
        for match in matches:
            print(match.group(0))
            if match.group(1) == '5':
                print "================================================================"
                print (bcolors.OKGREEN + "result of pinging %s from subnet %s is passed" % (fw_ip, gw_ip) + bcolors.ENDC)
                print "================================================================"
            elif match.group(1) == '4':
                print "================================================================"
                print (bcolors.OKGREEN + "result of pinging %s from subnet %s is passed" % (fw_ip, gw_ip) + bcolors.ENDC)
                print "================================================================"
            else:
                print "================================================================"
                print (bcolors.FAIL + "result of pinging %s from subnet %s is failed" % (fw_ip, gw_ip) + bcolors.ENDC)
                print "================================================================"
        # print "----- is output a string -------"
        # print isinstance(output, str)
    #print traffic_pattern.search(output)
    # remote_conn.send("route add -net %s gw %s\n" % (fw_net, gw_ip))
    # remote_conn.send("route -n\n")
    # remote_conn.send("scapy\n")
    # remote_conn.send("pingr=IP(dst=\"%s\")/ICMP()\n" % fw_ip)
    # remote_conn.send("resp_ping=srloop(pingr,count=5)\n")
    # remote_conn.send("resp_ping\n")
    # # Wait for the command to complete
    # time.sleep(10)
    
    # output = remote_conn.recv(5000)
    # print output

