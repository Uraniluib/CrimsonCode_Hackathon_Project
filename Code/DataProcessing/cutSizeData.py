# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:32:11 2019

@author: xingg
"""

file = open('..\\rawDataStep2.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\rawDataStep3.csv','w',encoding = 'utf-8')

for line in lines:
    ls = line.split('\t')
    counter = 0
    for l in ls: 
        if (l == 'NA'): 
            counter += 1
    if counter <= 7 and 'User' not in ls[1]:
        writeFile.write(ls[0])
        for i in range(1,len(ls)):
            writeFile.write('\t'+ls[i])

writeFile.close()