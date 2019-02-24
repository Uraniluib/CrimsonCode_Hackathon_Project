# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 15:50:31 2019

@author: xingg
"""

file = open('..\\Full_Info_Data.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\IdWithTitle.csv','w',encoding = 'utf-8')

for line in lines:
    ls = line.split('\t')
    writeFile.write(ls[0]+ '\t' +ls[1]+'\n')
writeFile.close()