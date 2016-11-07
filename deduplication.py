'''
1、对特定文件内容进行去重操作
2、请输入需要去重文件的绝对路径
3、删除文件中的空行
4、去除字符串前后空行
5、生成一个以当前日期命名的文件
'''

import time

year = time.localtime().tm_year
mon = time.localtime().tm_mon
day = time.localtime().tm_mday
hour = time.localtime().tm_hour
min = time.localtime().tm_min
sec = time.localtime().tm_sec
nowtime = str(year) + str(mon) + str(day) + str(hour) + str(min) + str(sec)

f = input("please entry the file[absolute path]:")

def openThefile():
    '''
    1、打开要去重的文件
    2、删除每行数据前后的无用字符
    :return:
    '''
    ff = open(f,'r')
    l = []
    #for i in ff.readline():     #readline是文件中的第一行内容
    for i in ff.readlines():    #所有内容中的每一行
        ii = i.replace('\t','').strip()
        l.append(ii)
    ff.close()
    return l

def createNewfile(openThefile):
    '''
    去重操作
    :param openThefile:
    :return:
    '''
    l = []
    for i in openThefile:
        if i not in l:
            l.append(i)
    '''
    创建新文件
    '''
    filename = f[:f.find('.')]
    postfix = f[f.find('.'):]
    theNewfile = open(filename + nowtime + postfix,'a')
    '''
    写入处理过的内容
    '''
    for i in l:
        theNewfile.writelines(i+'\n')
    theNewfile.close()



if __name__ == '__main__':
    createNewfile(openThefile())