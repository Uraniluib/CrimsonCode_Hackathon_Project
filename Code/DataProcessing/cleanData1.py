# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 08:43:10 2019

@author: xingg
"""

import re

file = open('..\\rawDataStep1.csv','r',encoding = 'utf-8')

lines = file.readlines()

writeFile = open('..\\rawDataStep1_2.csv','w',encoding = 'utf-8')

for line in lines:
    ls = line.split('\t')
    writeFile.write(ls[0])
    for i in range(1,len(ls)):
        #| RealName 
        if "| RealName" in line:
            ls[i] = re.sub('(?<=| RealName).*(?<== )', '', ls[i])
        
        #| CurrentAlias
        if "| CurrentAlias" in line:
            ls[i] = re.sub('(?<=| CurrentAlias).*(?<== )', '', ls[i])
        
        #| Affiliation
        if "| Affiliation" in line:
            ls[i] = re.sub('(?<=| Affiliation).*(?<== )', '', ls[i])
        
        #| Relatives
        if "| Relatives" in line:
            ls[i] = re.sub('(?<=| Relatives).*(?<== )', '', ls[i])
        
        #| Universe
        if "| Universe" in line:
            ls[i] = re.sub('(?<=| Universe).*(?<== )', '', ls[i])
        
        #| Gender
        if "| Gender" in line:
            ls[i] = re.sub('(?<=| Gender).*(?<== )', '', ls[i])
        
        #| Height
        if "| Height" in line:
            ls[i] = re.sub('(?<=| Height).*(?<== )', '', ls[i])
        
        #| Weight
        if "| Weight" in line:
            ls[i] = re.sub('(?<=| Weight).*(?<== )', '', ls[i])
        
        #| Eyes
        if "| Eyes" in line:
            ls[i] = re.sub('(?<=| Eyes).*(?<== )', '', ls[i])
        
        #| Hair
        if "| Hair" in line:
            ls[i] = re.sub('(?<=| Hair).*(?<== )', '', ls[i])
        
        #| Citizenship 
        if "| Citizenship" in line:
            ls[i] = re.sub('(?<=| Citizenship).*(?<== )', '', ls[i])
        	
        #| Quotation
        if "| Quotation" in line:
            ls[i] = re.sub('(?<=| Quotation).*(?<== )', '', ls[i])
        
        writeFile.write('\t'+ls[i])
    #writeFile.write('\t'+ls[len(ls)-1] + '\n')

writeFile.close()

        
