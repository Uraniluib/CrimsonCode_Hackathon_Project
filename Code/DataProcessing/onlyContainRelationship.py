# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:01:06 2019

@author: xingg
"""

import re

file = open('..\\Full_Info_Data.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\onlyContaionRelationship.csv','w',encoding = 'utf-8')

for line in lines:
    ls = line.split('\t')
    if ls[5] != 'NA':
        writeFile.write(ls[0]+'\t'+re.sub('[ (].*[)]', '', ls[1])+'\t'+ls[5]+'\n')

writeFile.close()