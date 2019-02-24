# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:46:21 2019

@author: xingg
"""
import re

file = open('..\\rawDataStep1.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\rawDataStep2.csv','w',encoding = 'utf-8')

for line in lines:
    ls = line.split('\t')
    writeFile.write(ls[0])
    for i in range(1,len(ls)):
        if ls[i] == '':
            writeFile.write('\tNA')
        else:
            ls[i] = re.sub('(?<=&lt;ref&gt;).*(?<=&lt;/ref&gt;)', '', ls[i])
            writeFile.write('\t'+ls[i])
    #writeFile.write('\t'+ls[len(ls)-1] + '\n')

writeFile.close()