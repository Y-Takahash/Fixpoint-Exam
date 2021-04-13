#設問2
import datetime

def main_2(N):
    file = open("log2.txt","r",encoding = "utf_8")
    log = file.read().split('\n')
    date_format = '%Y%m%d%H%M%S' 
    date_dict = {} #アドレス-最初にタイムアウトした日時の辞書
    
    
    for line in log:
        splited = line.split(',')
        if splited[2] == '-':
            if splited[1] not in date_dict:
                outdate = datetime.datetime.strptime(splited[0],date_format)
                date_dict[splited[1]] = [outdate]
                continue
            else:
                date_dict[splited[1]].append(outdate)
            
        else:
            if splited[1] in date_dict:
                if len(date_dict[splited[1]]) >= N:
                    logdate = datetime.datetime.strptime(splited[0],date_format)
                    diff = logdate - date_dict[splited[1]][0]
                    print(str(splited[1]),"---",str(diff.total_seconds()))
                del date_dict[splited[1]] 
    file.close()
main_2(3)