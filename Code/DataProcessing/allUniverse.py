# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 19:08:02 2019

@author: xingg
"""

file = open('..\\Full_Info_Data.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\allUniverse.csv','w',encoding = 'utf-8')

universe = set()

for line in lines:
    ls = line.split('\t')
    universe.add(ls[6].replace('[[','').replace(']]','').replace('(','').replace(')','').replace(' ',''))
    
universe = list(universe)
universe.sort()

for u in universe: 
    writeFile.write(u+'\n')
writeFile.close()

