import re,os
def main():
    f= open("guru99.txt","w+")
    #f=open("guru99.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    f=open("putty.log", "r")
    if f.mode == 'r':
        contents =f.read()
    #move the pointer to the target position
    #print(f.tell())
    f.seek(0)
    #print(f.tell())
    #or, readlines reads the individual line into a list
    fl =f.readlines()
    flag=0
    tep = []
    sen = []
    ##print(fl)
    for ss in fl:
        #print(ss)
        if ss=="-> show -level all -output table /SYS type==Temperature value\n":
            print('===Start of sentence ========')
            flag = 1
            #clear old log
            tep = []
            sen = []

        if flag ==1:
            #print('ss:\n', ss)
            s = re.sub(r"\s+", "", ss)
            #print('s:\n', s)
            m = re.search('([0-9]+\.[0-9]+)',s)
            #print('m:\n', m)
            if (m):
                #print(m.group())
                tep.append(m.group())
                #print(ss)
                sen.append(ss)
        if ss=="-> show /SP/network -t -l 2 ipaddress ipnetmask ipgateway\n":
            print(tep)
            #print(sen)
            print("===End of sentence===")
            print('MAX temperature:', max(tep), 'degree C')
            flag = 0
    #print(tep)
    #all temperature
    if(tep != []):
        #print('MAX temperature:', max(tep), 'degree C')
        f1 = open('test.txt', 'w')
        f1.write('MAX temperature:  ' + max(tep) + '  degree C')
        f2 = open('putty.log', 'r')
        fq = open('b.txt','w')		
        for line in sen:
           fq = open('b.txt','a')#這裡用追加模式
           #fq.write('\n')
           fq.write(line)
        f2.close()
        fq.close()
    else:
        print('putty.log is empty!,re-run the temperature program!')
    #print('cmd')
    #cmd = 'python D:\tsungwu\readtemperature\tenpeerature.py'
    #r = os.popen(cmd)
    #print(r)
    #sys.stdout.write('MAX temperature:',max(tep),'degree C')
if __name__== "__main__":
  main()