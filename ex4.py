#設問4
import datetime
from collections import defaultdict, deque

def conv(string):
    date_format = '%Y%m%d%H%M%S'
    conv_ret = datetime.datetime.strptime(string,date_format)
    return conv_ret

def main_4(N):
    file = open("log4.txt","r",encoding = "utf_8")
    log = file.read().split('\n')
    subnet = defaultdict()
    
    for line in log:
        splited = line.split(',')
        ip,sub = splited[1].split('/')
        ip_bin = ''.join([format(int(d),'08b') for d in ip.split('.')])

        if str(ip_bin[:int(sub)]) not in subnet: 
            subnet[str(ip_bin[:int(sub)])] = []
        subnet[str(ip_bin[:int(sub)])].append((conv(splited[0]),splited[2]))

    for k in subnet.keys():
        count = 0
        for i,d in enumerate(subnet[k]):
            if d[1] == '-':
                count += 1
            else:
                if count >= N:
                    print('.'.join([str(int('{:0<32}'.format(k)[j:j+8],2)) for j in range(0,32,8)]), "---",subnet[k][i][0] - subnet[k][i-count][0])
                    #↑桁数32桁で0埋めしたIP（2進数）を8桁区切りでint()を用いて10進数のIPに戻し、
                    #通信が復活した時刻(subnet[k][i][0])-通信が連続してタイムアウトした初回の時刻（subnet[k][i-count][0]）
                count = 0
    file.close()
    
main_4(2)