#coding=utf-8
'''
Created on 2015/7/31

@author: fmir55
'''

import sys

myfo = open('/mnt/hgfs/下載/NYPD_Motor_Vehicle_Collisions.csv', 'r')
result = list()  
i=1
for line in open('/mnt/hgfs/下載/NYPD_Motor_Vehicle_Collisions.csv'):  
    line = myfo.readline()  
    if  line.split(',')[2]!='':
        if i!=1:
            line=line.split(',')[0]+' '+line.split(',')[1]+','+line.split(',')[4]+','+line.split(',')[5]+','+line.split(',')[11]
        else:
            line=line.split(',')[0]+','+line.split(',')[4]+','+line.split(',')[5]+','+line.split(',')[10]
        result.append(line)  
    print i
    i=i+1
    if i==1500000:
        break
myfo.close()                  
print "Sucessfully Formated"
open('/mnt/hgfs/下載/NYPD_Motor_Vehicle_Collisions333.csv', 'w').write('%s' % '\n'.join(result))

