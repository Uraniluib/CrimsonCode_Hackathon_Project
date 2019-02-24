# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 20:17:17 2019

@author: xingg
"""

fileUniverse = open('..\\allUniverse.csv','r',encoding = 'utf-8')

fileInfo = open('..\\Full_Info_Data.csv','r',encoding = 'utf-8')

writeFile = open('..\\idWithUniverse.csv','w',encoding = 'utf-8')

universes = fileUniverse.readlines()

universe = universes[0].split('\t')

lines = fileInfo.readlines()

for line in lines:
    info = line.split('\t')
    temp = ''
    for u in universe:
        if u in info[6]:
            temp = info[0] + '\t' + u + '\n'
    writeFile.write(temp)
        
writeFile.close()
