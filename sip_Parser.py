import string
import sys
import hash

f=open('1.txt_filtered.txt')



list

def sip_Addresses():
    f0=open('sipaddress.txt','w')
    linecontroller=0
    count=0
    for line in f:
       # if(line.find('Session Initiation Protocol')!=-1):

        if(line.find('Request-Line:')!=-1):
            print(line)
            count=count+1
        elif(line.find('-Line:')!=-1):
            print(line)
            linecontroller=1
            count=count+1
        if(linecontroller==1):
            if(line.find('SIP from address:')!=-1):
                #print(line)
                print(line.split(':',3)[2])
                f0.write(line.split(':',3)[2])
                linecontroller=0

    f0.close()

#print (count)


def get_Sip_Addresses():
    c=0
    list2=[]
    f0=open('sipaddress.txt','r')
    print(f0)

    for line in f0:

        list2.append(line)
        #print(list2.__getitem__(c))
        c=c+1
        if(c==1000):
            f0.close()
            return list2
'''
sip_Addresses()
get_Sip_Addresses()
print("ksakdka")
'''