#İ–â3
from collections import defaultdict, deque
import statistics
import datetime
def conv(string):
    date_format = '%Y%m%d%H%M%S'
    conv_ret = datetime.datetime.strptime(string,date_format)
    return conv_ret

def main_3(m,t):
    file = open("log3.txt","r",encoding = "utf_8")
    log = file.read().split('\n')
    fail_dict = defaultdict()
    load_dict = defaultdict()

    for line in log:
        splited = line.split(',')
        if splited[2] != '-':
            if splited[1] not in fail_dict:
                fail_dict[splited[1]] = deque()

            if len(fail_dict[splited[1]]) >= m-1:
                fail_dict[splited[1]].append(int(splited[2]))

                mean = statistics.mean(fail_dict[splited[1]])

                if mean < t and splited[1] in load_dict:
                    print(str(splited[1]),'---',conv(splited[0]) - load_dict[splited[1]])

                else:
                    if splited[1] not in load_dict:
                        load_dict[splited[1]] = conv(splited[0])
                fail_dict[splited[1]].popleft()
            else:
                fail_dict[splited[1]].append(int(splited[2]))
    file.close()

main_3(2,2)