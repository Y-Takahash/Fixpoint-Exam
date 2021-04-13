#設問1
import datetime
file = open("log1.txt","r",encoding = "utf_8")
log = file.read().split('\n')
date_format = '%Y%m%d%H%M%S'
address_dict = {} #各サーバーアドレス-最初のタイムアウト時刻の辞書
for line in log:
    splited = line.split(',')
    if splited[2] == '-':
        if splited[1] not in address_dict:
            address_dict[splited[1]] = datetime.datetime.strptime(splited[0], date_format)
        continue
    if splited[1] in address_dict.keys():
        if splited[2] != '-':
            logdate = datetime.datetime.strptime(splited[0],date_format)
            diff = logdate - address_dict[splited[1]] #復帰時刻と最初のタイムアウト時刻の差分
            print(str(splited[1]),"---",str(diff.total_seconds()))
            del address_dict[splited[1]] #辞書からキーを削除
file.close()
    